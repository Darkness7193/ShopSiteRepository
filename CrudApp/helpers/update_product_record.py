from CrudApp.models import Product
from decimal import Decimal


def update_product_record(request):
    update_id = request.POST.get('update_id')

    if update_id:
        product = Product.objects.get(id=update_id)
        product.name = request.POST.get('name')
        product.price = Decimal(request.POST.get('price'))
        product.description = request.POST.get('description')[:200]
        product.count = request.POST.get('count')
        product.save()
