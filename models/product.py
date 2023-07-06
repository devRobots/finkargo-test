"""
Modelo de Usuario en la base de datos
"""
from typing import Optional

class User:
    """
    Definicion de la clase Usuario
    """
    id: Optional[str]
    description: str
    price: float
    stock: int

    def __init__(self, description: str, price: float, stock: int):
        self.description = description
        self.price = price
        self.stock = stock

    def json(self):
        """
        Return the object as a json
        """
        return {
            '_id': {
                '$oid': self.id
            },
            'description': self.description,
            'price': self.price,
            'stock': self.stock
        }
