"""
Pruebas unitarias del servicio de balance
"""
import pytest
from utils.files import load_json_data
from services.sort import sort_items_service

@pytest.mark.parametrize(
    "items, expected",
    [
        (
            load_json_data("sort_service_input"),
            load_json_data("sort_service_expected")
        )
    ]
)
def test_make_balance_service(items, expected):
    """
    Prueba unitaria del servicio de balance
    """
    sort = sort_items_service(items)
    assert sort == expected
