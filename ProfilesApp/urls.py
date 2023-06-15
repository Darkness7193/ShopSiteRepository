from django.urls import path
from ProfilesApp.views import (
    log_in,
    sign_in,
    log_out,
    password_change,
    username_change,
    user_status_change,
    delete_user,
)

urlpatterns = [
    path('log-in/', log_in, name='log-in'),
    path('sign-in/', sign_in, name='sign-in'),
    path('log-out/', log_out, name='log-out'),
    path('password-change/', password_change, name='password-change'),
    path('username-change/', username_change, name='username-change'),
    path('user-status-change/', user_status_change, name='user-status-change'),
    path('delete-user/', delete_user, name='delete-user'),
]