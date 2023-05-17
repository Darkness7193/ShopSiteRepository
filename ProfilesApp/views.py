from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Profile
from ShopSite.MyShortcuts import get_or_none


def log_in(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Логин или пароль введен неверно')
            return HttpResponseRedirect(request.path_info)
        else:
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

        is_login_exist = get_or_none(User, username=username)

        errors = []
        if password != password_conf:
            errors.append('Введенные пароли не совпадают')
        if is_login_exist:
            errors.append('Введенный логин уже используется')

        if errors:
            for error_content in errors:
                messages.error(request, error_content)
            return HttpResponseRedirect(request.path_info)
        else:
            user = User(username=username)
            user.set_password(password)
            user.save()
            profile = Profile(user=user)
            profile.save()
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

        errors = []
        if password != password_conf:
            errors.append('Введенные пароли не совпадают')
        if not user.check_password(old_password):
            errors.append('Введенный пароль не совпадает с старым паролем')

        if errors:
            for error_content in errors:
                messages.error(request, error_content)
            return HttpResponseRedirect(request.path_info)
        else:
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        return render(request, 'ProfilesApp/password-change.html')
