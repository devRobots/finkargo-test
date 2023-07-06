"""
Pruebas unitarias del servicio de usuarios
"""
import pytest

from utils.files import load_json_data
from tests.mock import mock_flask, mock_pymongo

from services.users import list_users_service, get_user_service
from services.users import add_user_service, update_user_service
from services.users import delete_user_service

@pytest.mark.parametrize(
    "expected",
    [(load_json_data("list_users_service_expected"))]
)
def test_list_users_services(mocker, expected):
    """
    Prueba unitaria del servicio de listado de usuarios
    """
    mock_flask(mocker)
    mock_pymongo(mocker)
    users, status = list_users_service()
    assert status == 500

@pytest.mark.parametrize(
    "user_id, expected",
    [(1, load_json_data("get_user_service_expected"))]
)
def test_get_user_service(mocker, user_id, expected):
    """
    Prueba unitaria del servicio de obtener un usuario
    """
    mock_flask(mocker)
    mock_pymongo(mocker)
    user, status = get_user_service(user_id)
    assert status == 500

@pytest.mark.parametrize(
    "input_data",
    [(load_json_data("add_user_service_input"))]
)
def test_add_user_service(mocker, input_data):
    """
    Prueba unitaria del servicio de agregar un usuario
    """
    mock_flask(mocker)
    mock_pymongo(mocker)
    user_id, status = add_user_service(input_data)
    assert status == 500

@pytest.mark.parametrize(
    "user_id, input_data",
    [(1, load_json_data("update_user_service_input"))]
)
def test_update_user_service(mocker, user_id, input_data):
    """
    Prueba unitaria del servicio de actualizar un usuario
    """
    mock_flask(mocker)
    mock_pymongo(mocker)
    message, status = update_user_service(user_id, input_data)
    assert status == 500

@pytest.mark.parametrize("user_id", [(1)])
def test_delete_user_service(mocker, user_id):
    """
    Prueba unitaria del servicio de eliminar un usuario
    """
    mock_flask(mocker)
    mock_pymongo(mocker)
    message, status = delete_user_service(user_id)
    assert status == 500
