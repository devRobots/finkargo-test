"""
User model on MongoDB
"""
from typing import Optional

class User:
    """
    User model definition
    """
    id: Optional[str]
    descripcion: str
    precio: float
    stock: int

    def __init__(self, descripcion: str, precio: float, stock: int):
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def json(self):
        """
        Return the object as a json
        """
        return {
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock
        }
