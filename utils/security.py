"""
Utilidades para la seguridad de la aplicacion
"""
from base64 import b64decode, binascii
from flask import Flask, request, make_response

def basic_auth(func):
    """
    Funcion decoradora para verificar si la autenticacion es valida
    """
    def wrapper(*args, **kwargs):
        app_config = Flask('__main__').config
        app_config.from_prefixed_env()

        auth = request.headers.get('Authorization')
        header = {"WWW-Authenticate": 'Basic realm="Login Required"'}

        if not auth:
            return make_response('Autorizacion no encontrada', 403, header)

        auth = auth.split(" ")

        if auth[0] != 'Basic':
            return make_response('El tipo de autorizacion no es valida', 403, header)

        try:
            username, password = b64decode(auth[1]).decode('utf-8').split(":")
        except binascii.Error:
            return make_response('La autorizacion no es valida', 403, header)

        if username != app_config['BASIC_AUTH_USERNAME']:
            return make_response('El nombre de usuario es incorrecto', 403, header)
        if password != app_config['BASIC_AUTH_PASSWORD']:
            return make_response('La clave es incorrecta', 403, header)

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper
