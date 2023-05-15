from django.urls import path
from app.views import crud, delete_product, create_product, update_product

urlpatterns = [
    path('crud/', crud, name='crud'),
    path('delete_product/', delete_product, name='delete_product'),
    path('create_product/', create_product, name='create_product'),
    path('update_product/', update_product, name='update_product'),
]
