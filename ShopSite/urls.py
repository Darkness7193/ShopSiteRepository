from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('app/', include('app.urls')),
    path('ProfilesApp/', include('ProfilesApp.urls')),
]
