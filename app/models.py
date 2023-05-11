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
    image = ImageField()
    #category = ForeignKey()

    def __str__(self):
        return str(self.name) + str(self.price)

    class Meta:
        db_table = 'Product'


class Category(Model):
    objects = MyManager()

    name = CharField(max_length=20)
    description = CharField(max_length=400)
    image = ImageField()

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'Category'