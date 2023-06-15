from CrudApp.models import Product, RecordSave
from decimal import Decimal


def create_reset(save):
    Product.objects.filter(id=int(save.product_id)).delete()


def delete_reset(save):
    product = Product(
        id=int(save.product_id),
        name=save.name,
        price=Decimal(save.price),
        description=save.description,
        count=save.count,
    )
    product.save()


def update_reset(save):
    product = Product.objects.get(id=int(save.product_id))
    product.name = save.name
    product.price = Decimal(save.price)
    product.description = save.description
    product.count = save.count
    product.save()


def soft_reset(save_id):
    save = RecordSave.objects.get(id=save_id)

    if save.mode == 'create':
        create_reset(save)
    elif save.mode == 'delete':
        delete_reset(save)
    elif save.mode == 'update':
        update_reset(save)

    save.delete()
