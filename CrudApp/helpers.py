from CrudApp.models import Product, RecordSave
from decimal import Decimal
from django.http import HttpResponseRedirect


def get_searched_products(request):
    if request.method == 'POST':
        search_query = request.POST.get('products_search')
        searched_products = []

        for product in Product.objects.all():
            if search_query in product.__str__():
                searched_products.append(product)

        return searched_products
    else:
        return Product.objects.all()


def soft_reset(save_id):
    save = RecordSave.objects.get(id=save_id)

    if save.mode == 'create':
        Product.objects.filter(id=int(save.product_id)).delete()
    elif save.mode == 'delete':
        product = Product(
            id=int(save.product_id),
            name=save.name,
            price=Decimal(save.price),
            description=save.description,
            count=save.count,
        )
        product.save()
    elif save.mode == 'update':
        product = Product.objects.get(id=int(save.product_id))
        product.name = save.name
        product.price = Decimal(save.price)
        product.description = save.description
        product.count = save.count
        product.save()

    save.delete()


def reload_page(request):
    HttpResponseRedirect(request.path_info)
