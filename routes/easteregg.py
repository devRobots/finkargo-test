"""
Ruta de API para un huevo de pascua
"""
from flask import Blueprint

easteregg_route = Blueprint('easteregg_route', __name__)

@easteregg_route.route('/easteregg', methods=['GET'])
def sort_items():
    """
    Ruta para un huevo de pascua
    """
    return "Hola Mundo!, este es un huevo de pascua. By: Yesid"
