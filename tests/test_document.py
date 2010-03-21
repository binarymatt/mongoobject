import unittest
from mongoobject import MongoObject
import pymongo
class DocumentTest(unittest.TestCase):
    fixture = {'firstname': 'John', 'lastname': 'Doe', 'email': 'test@acme.com'}
    def test_create(self):
        Test = MongoObject.factory('create_tests')
        test = Test.create(self.fixture)
        assert isinstance(test, Test)
        assert hasattr(test, '__collection__')
        
    
    def test_get(self):
        Test = MongoObject.factory('tests')
        test = Test.get('4ba4d1f84fa08262e8000000')
        assert test._object_dict['firstname'] == 'John'
        assert test._object_dict['lastname'] == 'Doe'
    
    def test_find(self):
        Test = MongoObject.factory('find_tests')
        Test.__db__.drop_collection('find_tests')
        Test.create({'hello':'world'})
        Test.create({'hello2':'world2'})
        assert len(list(Test.find())) == 2
        assert len(list(Test.find({"hello":"world"}))) == 1
    
    def test_set_attribute(self):
        Test = MongoObject.factory('tests')
        test = Test.get('4ba4d1f84fa08262e8000000')
        test.phone = 6152898513
        assert test._object_dict.has_key('phone')
        assert test._object_dict['phone'] == 6152898513
    
    def test_get_attribute(self):
        Test = MongoObject.factory('tests')
        test = Test.get('4ba4d1f84fa08262e8000000')
        assert test.firstname == 'John'
        assert test.lastname == 'Doe'
    
    def test_save(self):
        Test = MongoObject.factory('save_tests')
        test = Test({'hello':'world'})
        test.save()
        assert test._object_dict.has_key('_id')
    
    def test_delete(self):
        database = pymongo.Connection().mongo_object
        collection = database.delete_tests
        Test = MongoObject.factory('delete_tests')
        test = Test.create({'hello':'world'})
        assert collection.count() == 1
        test.delete()
        assert collection.count() == 0
    
