"""
Sale model on MongoDB
"""
from typing import Optional

class Sale:
    """
    Sale model definition
    """
    id: Optional[str]
    usuario: str
    producto: str
    cantidad: int
    subtotal: float
    total: float

    def __init__(self, usuario: str, producto: str, cantidad: int, subtotal: float, total: float):
        self.usuario = usuario
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.total = total

    def json(self):
        """
        Return the object as a json
        """
        return {
            'usuario': self.usuario,
            'producto': self.producto,
            'cantidad': self.cantidad,
            'subtotal': self.subtotal,
            'total': self.total
        }
