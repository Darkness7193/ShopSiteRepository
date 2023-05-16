from django.urls import path
from django.views.generic import RedirectView

from .views import logIn, signIn, logOut


urlpatterns = [
    path('logIn/', logIn, name='logIn'),
    path('signIn/', signIn, name='signIn'),
    path('logOut/', logOut, name='logOut'),
    path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico'), name='favicon.ico')
]