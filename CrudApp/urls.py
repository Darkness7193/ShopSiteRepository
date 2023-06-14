from django.urls import path
from CrudApp.views import (
    crud,
    history,
    delete_product,
    create_product,
    update_product,
    save_in_history,
    strict_reset
)

urlpatterns = [
    path('crud/', crud, name='crud'),
    path('history/', history, name='history'),

    path('delete_product/', delete_product, name='delete_product'),
    path('create_product/', create_product, name='create_product'),
    path('update_product/', update_product, name='update_product'),
    path('save_in_history/', save_in_history, name='save_in_history'),
    path('strict_reset/', strict_reset, name='strict_reset'),
]
