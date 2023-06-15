from django.shortcuts import render, redirect
from django.urls import reverse

from CrudApp.models import RecordSave
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.cache import never_cache


from CrudApp.helpers import (
    create_product_record,
    delete_product_record,
    get_searched_products,
    soft_reset,
    update_product_record,
    create_save_record,
)


def index(request):
    return redirect(reverse('crud'))


@never_cache
def crud(request):
    context = {'products': get_searched_products(request)}
    return render(request, 'CrudApp/crud.html', context)


@never_cache
def history(request):
    current_date = None
    saves_group_by_date = []
    for save in RecordSave.objects.order_by('-date', '-time'):
        if save.date != current_date:
            current_date = save.date
            saves_group_by_date.append([])

        saves_group_by_date[-1].append(save)

    context = {'saves_group_by_date': saves_group_by_date}
    return render(request, 'CrudApp/history.html', context)


@csrf_exempt
def delete_product(request):
    delete_product_record(request)
    return JsonResponse({})


@csrf_exempt
def create_product(request):
    product_id = create_product_record(request)
    return JsonResponse({'new_product_id': product_id})


@csrf_exempt
def update_product(request):
    update_product_record(request)
    return JsonResponse({})


@csrf_exempt
def save_in_history(request):
    create_save_record(request)
    return JsonResponse({})


@csrf_exempt
def strict_reset(request):
    saves = RecordSave.objects.order_by('-date', '-time')
    select_save_id = int(request.POST.get('save_id'))

    for save in saves:
        soft_reset(save.id)

        if save.id == select_save_id:
            break
    # Ajax mess up it and I'm dont want fix it
    return redirect(reverse('history'))
