"""
Modelo de Venta en la base de datos
"""
from typing import Optional

class Sale:
    """
    Definicion de la clase Venta
    """
    id: Optional[str]
    user_id: str
    product_id: str
    amount: int
    subtotal: float
    total: float

    def __init__(self, user_id: str, product_id: str, amount: int, subtotal: float, total: float):
        self.user_id = user_id
        self.product_id = product_id
        self.amount = amount
        self.subtotal = subtotal
        self.total = total

    def json(self):
        """
        Return the object as a json
        """
        return {
            '_id': {
                '$oid': self.id
            },
            'user_id': self.user_id,
            'product_id': self.product_id,
            'amount': self.amount,
            'subtotal': self.subtotal,
            'total': self.total
        }
