from django.contrib import admin
from django.urls import path, include
from CrudApp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('CrudApp/', include('CrudApp.urls')),
    path('ProfilesApp/', include('ProfilesApp.urls')),
]
