from django.contrib import admin
from django.urls import path, include
from app.views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]