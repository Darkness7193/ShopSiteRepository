from django.shortcuts import render, redirect
from django.urls import reverse
from CrudApp.models import Product, RecordSave
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from CrudApp.helpers import get_searched_products
from django.db.models.functions import TruncMonth
from django.db.models import Count


def index(request):
    return redirect(reverse('crud'))


@never_cache
def crud(request):
    context = {'products': get_searched_products(request)}
    return render(request, 'CrudApp/crud.html', context)


def history(request):
    current_date = None
    saves_group_by_date = []
    for save in RecordSave.objects.order_by('date'):
        if save.date != current_date:
            current_date = save.date
            saves_group_by_date.append([])

        saves_group_by_date[-1].append(save)


    context = {'saves_group_by_date': saves_group_by_date}
    return render(request, 'CrudApp/history.html', context)


@csrf_exempt
def delete_product(request):
    Product.record_delete(request)
    return JsonResponse({})


@csrf_exempt
def create_product(request):
    product_id = Product.create(request)
    return JsonResponse({'new_product_id': product_id})


@csrf_exempt
def update_product(request):
    Product.update(request)
    return JsonResponse({})


@csrf_exempt
def save_in_history(request):
    RecordSave.save_in_history(request)
    return JsonResponse({})
