from django.shortcuts import render, redirect
from django.urls import reverse
from CrudApp.models import Product, RecordSave
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decimal import Decimal
from datetime import datetime
from django.views.decorators.cache import never_cache


def index(request):
    return redirect(reverse('crud'))


@never_cache
def crud(request):
    if request.method == 'POST':
        search_query = request.POST.get('products_search')
        searched_products = []
        for product in Product.objects.all():
            if search_query in product.__str__():
                searched_products.append(product)
        context = {'products': searched_products}
    else:
        context = {'products': Product.objects.all()}

    return render(request, 'CrudApp/crud.html', context)


def history(request):
    context = {'record_saves': RecordSave.objects.all()}
    return render(request, 'CrudApp/history.html', context)


@csrf_exempt
def delete_product(request):
    delete_id = request.POST.get('delete_id')

    if delete_id:
        Product.objects.filter(id=int(delete_id)).delete()

    return JsonResponse({})


@csrf_exempt
def create_product(request):
    price = request.POST.get('price')
    product = Product(
        name=request.POST.get('name'),
        price=Decimal(price),
        description=request.POST.get('description'),
        count=request.POST.get('count'),
    )
    product.save()
    return JsonResponse({'new_product_id': product.id})


@csrf_exempt
def update_product(request):
    update_id = request.POST.get('update_id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    descriptions = request.POST.get('description')
    count = request.POST.get('count')

    if update_id:
        product = Product.objects.get(id=update_id)

        if name:
            product.name = name
        if price:
            product.price = Decimal(price)
        if descriptions:
            product.description = descriptions
        if count:
            product.count = count

        product.save()

    return JsonResponse({})


@csrf_exempt
def save_in_history(request):
    price = request.POST.get('price')
    dt = datetime.fromtimestamp(float(request.POST.get('timestamp')))
    record_save = RecordSave()

    record_save.mode = request.POST.get('mode')
    record_save.product_id = request.POST.get('product_id')
    record_save.name = request.POST.get('name')
    record_save.description = request.POST.get('description')
    record_save.count = request.POST.get('count')
    record_save.date = dt.date()
    record_save.time = dt.time()
    if price:
        record_save.price = Decimal(price)

    record_save.save()

    return JsonResponse({})
