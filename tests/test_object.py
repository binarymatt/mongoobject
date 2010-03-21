import unittest
from mongoobject import MongoObject
import pymongo
class MongoObjectTest(unittest.TestCase):
    def test_connection(self):
        connection = MongoObject.connection()
        assert hasattr(MongoObject, '_connection')
        assert isinstance(connection, pymongo.Connection)
        assert isinstance(MongoObject._connection, pymongo.Connection)
        
    def test_db(self):
        db = MongoObject.db()
        assert hasattr(MongoObject, '_connection')
        assert isinstance(db, pymongo.database.Database)
        assert db.name == 'mongo_object'
        db = MongoObject.db('test')
        assert db.name == 'test'
    
    def test_factory(self):
        Contact = MongoObject.factory('contacts')
        assert hasattr(Contact, '__collection__')
        assert Contact.__collection__ == 'contacts'
        
        