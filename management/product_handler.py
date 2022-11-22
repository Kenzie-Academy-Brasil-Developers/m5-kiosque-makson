from menu import products
from collections import Counter

def get_product_by_id(id: int):           
    if type(id) != int:
        raise TypeError("product id must be an int")

    product_find = {}

    for product in products:
        if product["_id"] == id:
            product_find.update(product)
    
    return product_find


def get_products_by_type(t: str):
    if type(t) != str:
        raise TypeError("product type must be a str")

    products_types = []

    for product in products:
        if product["type"] == t:
            products_types.append(product)
    
    return products_types

def menu_report():
    products_count = len(products)
    types = []
    sum_prices = 0

    for product in products:
        types.append(product["type"])
        sum_prices += product["price"]

    values = list(Counter(types).values())
    keys = list(Counter(types).keys())
    index_max_value = values.index(max(values))
    average_price = round(sum_prices/products_count , 2)
    
    return f"Products Count: {products_count} - Average Price: ${average_price} - Most Common Type: {keys[index_max_value]}"


def add_product(list_products, **kwargs):
    id_list = []
    _id = 0

    for p in list_products:
        id_list.append(p["_id"])

    if len(id_list) < 1:
        _id = 1
    else:
        _id = sorted(id_list)[-1] + 1
    
    new_product = {**kwargs, "_id": _id}
    list_products.append(new_product)
    return new_product
