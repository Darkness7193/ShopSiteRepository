from django.contrib import messages
from ShopSite.MyShortcuts import get_or_none
from django.contrib.auth.models import User


def is_validated_log_in():
    pass


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


def is_validated_username_change():
    pass


def is_validated_password_change():
    pass