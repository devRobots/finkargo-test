"""
Modelo de Usuario en la base de datos
"""
from typing import Optional

class User:
    """
    Definicion de la clase Usuario
    """
    id: Optional[str]
    name: str
    email: str
    phone: str

    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def json(self):
        """
        Return the object as a json
        """
        return {
            '_id': {
                '$oid': self.id
            },
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }
