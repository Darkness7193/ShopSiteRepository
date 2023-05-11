from django.shortcuts import render
from app.models import Product, Category

def index(request):
    context = {
    }
    return render(request, 'app/index.html', context)


def create(request):
    context = {

    }
    return render(request, 'app/create.html', context)


def delete(request):
    context = {
    }
    return render(request, 'app/delete.html', context)


def show(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'app/show.html', context)


def update(request):
    context = {
    }
    return render(request, 'app/update.html', context)