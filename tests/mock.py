"""
Mocking module for the tests
"""

from tests.mocks.flask import FlaskMock
from tests.mocks.pymongo import MongoClientMock

def mock_flask(mocker):
    """
    Mocks the flask.Flask class
    """
    mocker.patch(
        "flask.Flask", 
        side_efect=FlaskMock
    )

def mock_pymongo(mocker):
    """
    Mocks the pymongo.MongoClient class
    """
    mocker.patch(
        "pymongo.MongoClient", 
        return_value=MongoClientMock("localhost")
    )
