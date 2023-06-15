from decimal import Decimal
from datetime import datetime
from CrudApp.models import RecordSave


def create_save_record(request):
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