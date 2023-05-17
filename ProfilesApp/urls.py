from django.urls import path
from ProfilesApp.views import log_in, sign_in, log_out, password_change, username_change


urlpatterns = [
    path('log-in/', log_in, name='log-in'),
    path('sign-in/', sign_in, name='sign-in'),
    path('log-out/', log_out, name='log-out'),
    path('password-change/', password_change, name='password-change'),
    path('username-change/', username_change, name='username-change'),
]