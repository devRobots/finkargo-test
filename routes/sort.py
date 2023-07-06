"""
Ruta de API para ordenar elementos
"""
from flask import Blueprint, request, make_response
from services.sort import sort_items_service
from utils.security import basic_auth

sort_route = Blueprint('sort_route', __name__)

@sort_route.route('/sort', methods=['GET'])
@basic_auth
def sort_items():
    """
    Obtiene los parametros JSON enviados por el cliente y 
    los envia al servicio de ordenamiento
    """
    data = request.get_json()
    items = data.get('sin_clasificar')

    if not data or not items:
        return make_response('No se ha enviado ningún elemento', 400)

    response = sort_items_service(items)
    return make_response(response, 200)
