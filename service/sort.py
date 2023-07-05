"""
Servicio de Endpoint que recibe una lista de elementos y los ordena
"""
from flask import make_response

def sort_items_service(items):
    """
    Ordena los elementos de la lista items
    """
    items_bag = []
    repetead_items = []
    for item in items:
        items_bag.append(item)
        if items_bag.count(item) > 1 and item not in repetead_items:
            repetead_items.append(item)

    sorted_items = list(set(sorted(items)))
    sorted_items.extend(repetead_items)

    return make_response({
        'sin_clasificar': items,
        'clasificados': sorted_items
    }, 200)
