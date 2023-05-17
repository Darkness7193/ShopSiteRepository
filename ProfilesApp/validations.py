from django.contrib import messages
from ShopSite.MyShortcuts import get_or_none
from django.contrib.auth.models import User
from django.db.models import Q


def sign_in_validation(request, username, password, password_conf):
    is_login_exist = get_or_none(User, username=username)
    error = False

    if password != password_conf:
        messages.error(request, 'Введенные пароли не совпадают')
        error = True
    if is_login_exist:
        messages.error(request, 'Введенный логин уже используется')
        error = True

    return request, error


def password_change_validation(request, old_password, password, password_conf):
    user = request.user
    error = False

    if password != password_conf:
        messages.error(request, 'Введенные пароли не совпадают')
    if not user.check_password(old_password):
        messages.error(request, 'Введенный пароль не совпадает с паролем аккаунта')

    return request, error


def username_change_validation(request, new_username, password):
    user = request.user
    is_login_exist = bool(User.objects.filter(~Q(id=user.id), username=new_username))
    error = False

    if is_login_exist:
        messages.error(request, 'Введенный логин уже используется')
        error = True
    if not user.check_password(password):
        messages.error(request, 'Введенный пароль не совпадает с паролем аккаунта')
        error = True

    return request, error
