"""
Database module to connect to the database
"""
from pymongo import MongoClient

def get_connection():
    """
    Get the connection to the database
    """
    db_username = "ysrosast"
    db_password = "crashb22"
    db_host = "cluster0.dxldpvr.mongodb.net"
    uri = f"mongodb+srv://{db_username}:{db_password}@{db_host}/"
    client = MongoClient(uri)

    return client.finkargo
