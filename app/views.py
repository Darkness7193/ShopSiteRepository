from django.shortcuts import render
from app.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    context = {
    }
    return render(request, 'app/index.html', context)


def crud(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'app/crud.html', context)


def print_post(get):
    print([
        get('name'),
        get('price'),
        get('description'),
        get('count')
    ])


@csrf_exempt
def delete_product(request):
    delete_id = request.POST.get('delete_id')

    if delete_id:
        print('delete_product', delete_id)
        Product.objects.filter(id=int(delete_id)).delete()

    return JsonResponse({})


@csrf_exempt
def create_product(request):
    product = Product(
        name=request.POST.get('name'),
        price=int(request.POST.get('price')),
        description=int(request.POST.get('description')),
        count=int(request.POST.get('count')),
    )
    product.save()
    return JsonResponse({})


@csrf_exempt
def update_product(request):
    update_id = request.POST.get('update_id')

    if update_id:
        product = Product.objects.get(int(d=update_id))

        print_post(request.POST.get)

        product.name = request.POST.get('name')
        product.price = int(request.POST.get('price'))
        product.description = int(request.POST.get('description'))
        product.count = int(request.POST.get('count'))

        product.save()

    return JsonResponse({})
