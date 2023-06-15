from CrudApp.models import Product


def delete_product_record(request):
    delete_id = request.POST.get('delete_id')

    if delete_id:
        Product.objects.filter(id=int(delete_id)).delete()
