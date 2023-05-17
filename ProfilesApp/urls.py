from django.urls import path
from django.views.generic import RedirectView

from .views import log_in, sign_in, log_out, password_change


urlpatterns = [
    path('log-in/', log_in, name='log-in'),
    path('sign-in/', sign_in, name='sign-in'),
    path('log-out/', log_out, name='log-out'),
    path('password-change/', password_change, name='password-change'),
]