from django.shortcuts import render
from app.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decimal import Decimal


def index(request):
    context = {
    }
    return render(request, 'app/index.html', context)


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

    return render(request, 'app/crud.html', context)


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
    return JsonResponse({})


@csrf_exempt
def update_product(request):
    update_id = request.POST.get('update_id')

    if update_id:
        product = Product.objects.get(id=update_id)

        product.name = request.POST.get('name')
        product.price = Decimal(request.POST.get('price'))
        product.description = request.POST.get('description')
        product.count = request.POST.get('count')

        product.save()

    return JsonResponse({})
