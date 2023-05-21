from django.shortcuts import render, redirect
from django.urls import reverse
from CrudApp.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decimal import Decimal


def index(request):
    return redirect(reverse('crud'))


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


@csrf_exempt
def delete_product(request):
    delete_id = request.POST.get('delete_id')

    if delete_id:
        Product.objects.filter(id=int(delete_id)).delete()

    return JsonResponse({})


@csrf_exempt
def create_product(request):
    product = Product(
        name=request.POST.get('name'),
        price=Decimal(request.POST.get('price')),
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
