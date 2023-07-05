"""
Security module to check if the token is valid
"""
import base64
from flask import Flask, request, make_response

def basic_auth(func):
    """
    Funcion decoradora para verificar si la autenticacion es valida
    """
    def decorated():
        app_config = Flask('__main__').config
        app_config.from_prefixed_env()

        auth = request.headers.get('Authorization')
        header = {"WWW-Authenticate": 'Basic realm="Login Required"'}

        if not auth:
            return make_response('Autorization is missing', 403, header)

        auth = auth.split(" ")

        if auth[0] != 'Basic':
            return make_response('Autorization type is invalid', 403, header)

        try:
            username, password = base64.b64decode(auth[1]).decode('utf-8').split(":")
        except base64.binascii.Error:
            return make_response('Autorization is invalid', 403, header)

        if username != app_config['BASIC_AUTH_USERNAME']:
            return make_response('Invalid username or password', 403, header)
        if password != app_config['BASIC_AUTH_PASSWORD']:
            return make_response('Invalid username or password', 403, header)

        return func()

    return decorated
