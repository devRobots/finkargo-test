"""
Pruebas unitarias del servicio de balance
"""
import pytest
from utils.files import load_json_data
from services.balance import make_balance_service

@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            load_json_data("balance_service_input"),
            load_json_data("balance_service_expected")
        )
    ]
)
def test_make_balance_service(input_data, expected):
    """
    Prueba unitaria del servicio de balance
    """
    months = input_data["Mes"]
    sales = input_data["Ventas"]
    expenses = input_data["Gastos"]

    balance = make_balance_service(months, sales, expenses)
    assert balance == expected
