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


@csrf_exempt
def delete_product(request):
    delete_id = request.POST.get('delete_id')
    Product.objects.filter(id=int(delete_id)).delete()

    return JsonResponse({})


@csrf_exempt
def create_product(request):
    print('create_product. Fields =', [
        request.POST.get('name'),
        request.POST.get('price'),
        request.POST.get('description'),
        request.POST.get('count'),
    ])
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

    product = Product.objects.filter(id=int(update_id))

    product.save()
    return JsonResponse({})