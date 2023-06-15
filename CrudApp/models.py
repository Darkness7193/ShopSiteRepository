from django.db.models import (Model, CharField, TimeField, DateField,
                              DecimalField, PositiveIntegerField, ForeignKey, DO_NOTHING)
from django.contrib.auth.models import User
from ShopSite.MyShortcuts import MyManager
from decimal import Decimal
from datetime import datetime


class Product(Model):
    objects = MyManager()

    name = CharField(max_length=20)
    price = DecimalField(max_digits=6, decimal_places=2)
    description = CharField(max_length=400)
    count = PositiveIntegerField()

    def __str__(self):
        return f'{self.name} {self.price} {self.description} {self.count}'

    class Meta:
        db_table = 'Product'


class RecordSave(Model):
    mode = CharField(
        max_length=30,
        choices=(
            ('create', 'create'),
            ('delete', 'delete'),
            ('update', 'update')
        ),
    )
    product_id = PositiveIntegerField()
    name = CharField(max_length=20)
    price = DecimalField(max_digits=6, decimal_places=2)
    description = CharField(max_length=400)
    count = PositiveIntegerField()
    salesmen = ForeignKey(User, on_delete=DO_NOTHING, null=True, blank=True)

    date = DateField()
    time = TimeField()

    def __str__(self):
        time = self.time.__str__()[:-3]
        return f'{self.mode} {self.date} {time} {self.name} {self.price} {self.description} {self.count} '

    class Meta:
        db_table = 'RecordSave'

    def ru_mode(self):
        if self.mode == 'create':
            return 'создано'
        elif self.mode == 'delete':
            return 'удалено'
        elif self.mode == 'update':
            return 'обновлено'

    @staticmethod
    def save_in_history(request):
        price = request.POST.get('price')
        dt = datetime.fromtimestamp(float(request.POST.get('timestamp')))
        record_save = RecordSave()

        record_save.mode = request.POST.get('mode')
        record_save.product_id = int(request.POST.get('product_id'))
        record_save.name = request.POST.get('name')
        record_save.description = request.POST.get('description')
        record_save.count = request.POST.get('count')
        record_save.date = dt.date()
        record_save.time = dt.time()
        record_save.salesmen = request.user
        if price:
            record_save.price = Decimal(price)

        record_save.save()
