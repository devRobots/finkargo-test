"""
User model on MongoDB
"""
from typing import Optional

class User:
    """
    User model definition
    """
    id: Optional[str]
    name: str
    email: str
    telefono: str

    def __init__(self, name: str, email: str, telefono: str):
        self.name = name
        self.email = email
        self.telefono = telefono

    def json(self):
        """
        Return the object as a json
        """
        return {
            'name': self.name,
            'email': self.email,
            'telefono': self.telefono
        }
