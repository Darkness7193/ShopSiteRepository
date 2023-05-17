from django.contrib import messages
from ShopSite.MyShortcuts import get_or_none
from django.contrib.auth.models import User
from django.db.models import Q


def sign_in_validation(request, username, password, password_conf):
    is_login_exist = get_or_none(User, username=username)

    errors = []
    if password != password_conf:
        errors.append('Введенные пароли не совпадают')
    if is_login_exist:
        errors.append('Введенный логин уже используется')

    if errors:
        for error_content in errors:
            messages.error(request, error_content)

    return request, errors != []


def password_change_validation(request, old_password, password, password_conf):
    user = request.user
    errors = []

    if password != password_conf:
        errors.append('Введенные пароли не совпадают')
    if not user.check_password(old_password):
        errors.append('Введенный пароль не совпадает с паролем аккаунта')

    if errors:
        for error_content in errors:
            messages.error(request, error_content)

    return request, errors != []


def username_change_validation(request, new_username, password):
    user = request.user

    is_login_exist = User.objects.filter(~Q(id=user.id), username=new_username) == []

    errors = []
    if is_login_exist:
        errors.append('Введенный логин уже используется')
    if not user.check_password(password):
        errors.append('Введенный пароль не совпадает с паролем аккаунта')

    if errors:
        for error_content in errors:
            messages.error(request, error_content)

    return request, errors != []
