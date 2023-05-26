from django.db.models import (ForeignKey, Model, CharField, IntegerField, TimeField, DateField,
                              CASCADE, FloatField, SET_NULL, BooleanField, ImageField, DecimalField,
                              PositiveIntegerField, OneToOneField)
from django.contrib.auth.models import User
from ShopSite.MyShortcuts import MyManager


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
    product_id = PositiveIntegerField(null=True)
    name = CharField(max_length=20, null=True)
    price = DecimalField(max_digits=6, decimal_places=2, null=True)
    description = CharField(max_length=400, null=True)
    count = PositiveIntegerField(null=True)

    date = DateField()
    time = TimeField()

    def __str__(self):
        return f'{self.mode} {self.name} {self.price} {self.description} {self.count}'

    class Meta:
        db_table = 'RecordSave'
