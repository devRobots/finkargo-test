"""
Ruta de API para obtener el balance de una cuenta
"""
from flask import Blueprint, request, make_response
from services.balance import make_balance_service
from utils.security import basic_auth

balance_route = Blueprint('balance_route', __name__)

@balance_route.route('/balance', methods=['GET'])
@basic_auth
def make_balance():
    """
    Obtiene los parametros JSON enviados por el cliente y
    los envia al servicio de balance
    """
    data = request.get_json()
    months = data.get('Mes')
    sales = data.get('Ventas')
    expenses = data.get('Gastos')

    if not data:
        return make_response('No se ha enviado ningún elemento', 400)
    if not months or not sales or not expenses:
        return make_response('No se ha enviado algún elemento', 400)

    response = make_balance_service(months, sales, expenses)
    return make_response(response, 200)
