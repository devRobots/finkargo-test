"""
Mocks the pymongo library
"""
from models.user import User

class MongoClientMock:
    """
    Mocks the MongoClient class from pymongo
    """
    def __init__(self, uri):
        self.uri = uri
        self.finkargo = MongoDBMock()

    def __call__(self):
        return self.uri

class MongoDBMock:
    """
    Mocks the MongoDB class from pymongo
    """
    def __init__(self):
        self.users = MongoCollectionMock()

class MongoCollectionMock:
    """
    Mocks the MongoCollection class from pymongo
    """
    def find(self):
        """
        Mocks the find method from pymongo
        """
        user1 = User("Juan", "juan@mail.com", "2104949")
        user2 = User("Pedro", "pedro@mail.com", "2104948")
        user3 = User("Maria", "maria@mail.com", "2104947")
        return list([user1, user2, user3])

    def find_one(self, query):
        """
        Mocks the find_one method from pymongo
        """
        user = User("Juan", "juan@gmail.com", "2104949")
        user.id = query["_id"]
        return user.json()

    def insert_one(self, data):
        """
        Mocks the insert_one method from pymongo
        """
        print(data)
        return 1

    def update_one(self, query, data):
        """
        Mocks the update_one method from pymongo
        """
        print(query)
        print(data)
        return True

    def delete_one(self, query):
        """
        Mocks the delete_one method from pymongo
        """
        print(query)
        return True
