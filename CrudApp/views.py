from django.shortcuts import render, redirect
from django.urls import reverse
from CrudApp.models import Product, RecordSave
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from CrudApp.helpers import get_searched_products


def index(request):
    return redirect(reverse('crud'))


@never_cache
def crud(request):
    context = {'products': get_searched_products(request)}
    return render(request, 'CrudApp/crud.html', context)


def history(request):
    context = {'record_saves': RecordSave.objects.all()}
    return render(request, 'CrudApp/history.html', context)


@csrf_exempt
def delete_product(request):
    Product.record_delete(request)
    return JsonResponse({})


@csrf_exempt
def create_product(request):
    id = Product.create(request)
    return JsonResponse({'new_product_id': id})


@csrf_exempt
def update_product(request):
    Product.update(request)
    return JsonResponse({})


@csrf_exempt
def save_in_history(request):
    RecordSave.save_in_history(request)
    return JsonResponse({})
