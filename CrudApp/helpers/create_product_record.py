from CrudApp.models import Product
from decimal import Decimal


def create_product_record(request):
    product = Product(
        name=request.POST.get('name'),
        price=Decimal(request.POST.get('price')),
        description=request.POST.get('description')[:200],
        count=request.POST.get('count'),
    )
    product.save()
    return product.id
