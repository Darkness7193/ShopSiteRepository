from django.contrib import admin
from django.urls import path
from app.views import create, delete, show, update, crud

urlpatterns = [
    path('create/', create, name='create'),
    path('delete/', delete, name='delete'),
    path('show/', show, name='show'),
    path('update/', update, name='update'),
    path('crud/', crud, name='crud'),
]