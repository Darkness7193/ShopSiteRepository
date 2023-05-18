from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from ShopSite.MyShortcuts import get_or_none
from ProfilesApp.models import Profile

from .models import Profile
from .validations import (sign_in_validation,
                          password_change_validation,
                          username_change_validation)


def log_in(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Логин или пароль введен неверно')
            return HttpResponseRedirect(request.path_info)

        logout(request)
        login(request, user)
        return redirect(reverse('index'))
    else:
        return render(request, 'ProfilesApp/log-in.html')


def sign_in(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        password_conf = form.get('password_conf')

        request, have_errors = sign_in_validation(request, username, password, password_conf)
        if have_errors:
            return HttpResponseRedirect(request.path_info)

        user = User(username=username)
        user.set_password(password)
        profile = Profile(user=user)

        user.save()
        profile.save()
        login(request, user)
        return redirect(reverse('index'))
    else:
        return render(request, 'ProfilesApp/sign-in.html')


def log_out(request):
    logout(request)
    return redirect(reverse('index'))


def password_change(request):
    if request.method == 'POST':
        form = request.POST
        old_password = form.get('old_password')
        password = form.get('password')
        password_conf = form.get('password_conf')
        user = request.user

        request, have_errors = password_change_validation(request, old_password, password, password_conf)
        if have_errors:
            return HttpResponseRedirect(request.path_info)

        user.set_password(password)
        user.save()
        login(request, user)
        return redirect(reverse('index'))
    else:
        return render(request, 'ProfilesApp/password-change.html')


def username_change(request):
    if request.method == 'POST':
        form = request.POST
        password = form.get('password')
        new_username = form.get('username')
        user = request.user

        request, have_errors = username_change_validation(request, new_username, password)
        if have_errors:
            return HttpResponseRedirect(request.path_info)

        user.username = new_username
        user.save()
        logout(request)
        login(request, user)
        return redirect(reverse('index'))
    else:
        return render(request, 'ProfilesApp/username-change.html')


def user_status_change(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        status = form.get('user-status-select')
        user = get_or_none(User, username=username)

        if user == None:
            messages.error(request, 'Логин не существует')
            return HttpResponseRedirect(request.path_info)

        profile = Profile.objects.get(user__username=username)
        profile.status = status
        profile.save()
        return redirect(reverse('index'))
    else:
        return render(request, 'ProfilesApp/user-status-change.html')
