"""
Utilidades para la base de datos
"""
from flask import Flask
from pymongo import MongoClient

def get_connection():
    """
    Obtiene la conexión a la base de datos
    """
    app_config = Flask('__main__').config
    app_config.from_prefixed_env()

    db_username = app_config['MONGODB_USERNAME']
    db_password = app_config['MONGODB_PASSWORD']
    db_host = app_config['MONGODB_HOST']
    uri = f"mongodb+srv://{db_username}:{db_password}@{db_host}/"

    client = MongoClient(uri)

    return client.finkargo
