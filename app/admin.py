from django.contrib import admin
from . import models
register = admin.site.register


register(models.Product)
register(models.Category)

#admin_nickname = 'admin', admin_password = 'admin'