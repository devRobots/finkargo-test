"""
Ruta de API para gestionar usuarios
"""
from flask import Blueprint, request, make_response, Response
from services.users import list_users_service, get_user_service
from services.users import add_user_service, update_user_service
from services.users import delete_user_service
from utils.security import basic_auth

users_route = Blueprint('users_route', __name__)

@users_route.route('/users', methods=['GET'])
@basic_auth
def list_users():
    """
    Devuelve la lista de usuarios
    """
    message, status = list_users_service()

    if not status == 200:
        return make_response(message, status)

    return Response(message, status=status, mimetype='application/json')

@users_route.route('/users/<user_id>', methods=['GET'])
@basic_auth
def get_user(user_id):
    """
    Devuelve un usuario por su id
    """
    message, status = get_user_service(user_id)
    return make_response(message, status)

@users_route.route('/users', methods=['POST'])
@basic_auth
def add_user():
    """
    Agrega un usuario
    """
    data = request.get_json()
    user = data.get('user')

    if not data or not user:
        return make_response('No se ha enviado ningún usuario', 400)

    message, status = add_user_service(user)
    return make_response(message, status)

@users_route.route('/users/<user_id>', methods=['PUT'])
@basic_auth
def update_user(user_id):
    """
    Actualiza un usuario por su id
    """
    data = request.get_json()
    user = data.get('user')

    if not data or not user:
        return make_response('No se ha enviado ningún usuario', 400)

    message, status = update_user_service(user_id, user)
    return make_response(message, status)

@users_route.route('/users/<user_id>', methods=['DELETE'])
@basic_auth
def delete_user(user_id):
    """
    Elimina un usuario por su id
    """
    message, status = delete_user_service(user_id)
    return make_response(message, status)
