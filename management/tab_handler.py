from menu import products

def calculate_tab(table: list):
    subtotal = 0

    for t in table:
        for product in products:
            if product["_id"] == t["_id"]:
                subtotal += product["price"] * t["amount"]

    return {"subtotal": f"${round(subtotal, 2)}"}
