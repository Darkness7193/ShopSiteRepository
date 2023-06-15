from importlib import import_module


def one_function_per_file():
    files = [
        'create_product_record',
        'delete_product_record',
        'update_product_record',
        'get_searched_products',
        'soft_reset',
    ]

    for file in files:
        import_module('.'+file, 'CrudApp.helpers')
        globals()[file] = getattr(globals()[file], file)


one_function_per_file()
