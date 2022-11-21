from menu import products

def get_product_by_id(id: int):
    product_find = {}

    for product in products:
        if product["_id"] == id:
            product_find.update(product)
    
    return product_find

def get_products_by_type(type: str):
    products_types = []

    for product in products:
        if product["type"] == type:
            products_types.append(product)
    
    return products_types

def menu_report():
    products_count = len(products)
    sum_prices = 0

    for product in products:
        sum_prices += product["price"]

    average_price = round(sum_prices/products_count , 2)
    
    print(f"Products Count: {products_count} - Average Price: ${average_price} - Most Common Type: falta" )
    ...

def add_product(list_products, **kwargs):
    id_list = []
    _id = 0

    for p in list_products:
        id_list.append(p["_id"])

    if len(id_list) < 1:
        _id = 1
    else:
        _id = sorted(id_list)[-1] + 1
    
    new_product = {**kwargs, "id": _id}
    products.append(new_product)
    return new_product
