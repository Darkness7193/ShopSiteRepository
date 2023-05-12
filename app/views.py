from django.shortcuts import render
from app.models import Product

def index(request):
    context = {
    }
    return render(request, 'app/index.html', context)


def crud(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'app/crud.html', context)