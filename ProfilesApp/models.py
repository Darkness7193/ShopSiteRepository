from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, FloatField, CharField

from ShopSite.MyShortcuts import MyManager


class Profile(Model):
    objects = MyManager()

    user = OneToOneField(User, on_delete=CASCADE)
    status = CharField(
        max_length=30,
        default='Покупатель',
        choices=(
            ('Пользователь', 'Пользователь'),
            ('Продавец', 'Продавец'),
            ('Администратор', 'Администратор')
        )
    )
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Profile'






