"""
Servicio de Endpoint para la gestión de usuarios
"""
from bson import json_util
from bson.objectid import ObjectId
from pymongo import errors as mongo_errors
from utils.database import get_connection

def list_users_service():
    """
    Lista los usuarios en la base de datos
    """
    try:
        database = get_connection()
        users = database.users.find()
    except mongo_errors.PyMongoError:
        return 'No fue posible conectarse a la BD', 500

    return json_util.dumps(users), 200

def get_user_service(user_id):
    """
    Obtiene un usuario de la base de datos
    """
    try:
        database = get_connection()
        user = database.users.find_one({'_id': ObjectId(user_id)})
    except mongo_errors.PyMongoError:
        return 'No fue posible conectarse a la BD', 500

    if not user:
        return 'Usuario no encontrado', 404

    return json_util.dumps(user), 200

def add_user_service(user):
    """
    Agregar un usuario a la base de datos
    """
    try:
        database = get_connection()
        result = database.users.insert_one(user)
    except mongo_errors.PyMongoError:
        return 'No fue posible conectarse a la BD', 500

    return f'Usuario {result.inserted_id} agregado', 201

def update_user_service(user_id, user):
    """
    Actualiza un usuario de la base de datos
    """
    try:
        database = get_connection()
        database.users.update_one({'_id': ObjectId(user_id)}, {'$set': user})
    except mongo_errors.PyMongoError:
        return 'No fue posible conectarse a la BD', 500

    return f'Usuario {user_id} actualizado', 200

def delete_user_service(user_id):
    """
    Elimina un usuario de la base de datos
    """
    try:
        database = get_connection()
        database.users.delete_one({'_id': ObjectId(user_id)})
    except mongo_errors.PyMongoError:
        return 'No fue posible conectarse a la BD', 500

    return f'Usuario {user_id} eliminado', 200
