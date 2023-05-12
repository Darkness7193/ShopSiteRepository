from django.contrib import admin
from django.urls import path
from app.views import crud

urlpatterns = [
    path('crud/', crud, name='crud'),
]