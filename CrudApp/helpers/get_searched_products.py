from CrudApp.models import Product


def get_searched_products(request):
    if request.method == 'POST':
        search_query = request.POST.get('products_search')
        searched_products = []

        for product in Product.objects.all():
            if search_query in product.__str__():
                searched_products.append(product)

        return searched_products
    else:
        return Product.objects.all()
