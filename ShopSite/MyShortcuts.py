from django.db.models import Manager
from django.core.exceptions import ObjectDoesNotExist

class MyManager(Manager):

    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except ObjectDoesNotExist:
            return None


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except ObjectDoesNotExist:
        return None


def list_to_queryset(model, lst):
    return model.objects.filter(id__in=lst)