import unittest
from mongoobject import MongoObject
import pymongo
class DocumentTest(unittest.TestCase):
    fixture = {'firstname': 'John', 'lastname': 'Doe', 'email': 'test@acme.com'}
    def setUp(self):
        pass
    
    def tearDown(self):
        Test = MongoObject.factory('tests')
        Test.__db__.drop_collection('tests')
    
    def test_create(self):
        Test = MongoObject.factory('create_tests')
        test = Test.create(self.fixture)
        assert isinstance(test, Test)
        assert hasattr(test, '__collection__')
        
    def test_get(self):
        Test = MongoObject.factory('tests')
        Test.create(self.fixture)
        test = Test.find_one()
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
        Test.create(self.fixture)
        test = Test.find_one()
        test.phone = 6152898513
        assert test._object_dict.has_key('phone')
        assert test._object_dict['phone'] == 6152898513
    
    def test_attributes(self):
        Test = MongoObject.factory('tests')
        Test.create(self.fixture)
        test = Test.find_one()
        assert test
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
        Test.__db__.drop_collection('delete_tests')
        test = Test.create({'hello':'world'})
        assert collection.count() == 1
        test.delete()
        assert collection.count() == 0
    
    def test_getattr(self):
        Test = MongoObject.factory('attr_tests')
        Test.create(self.fixture)
        test = Test.find_one()
        assert test.firstname == 'John'
        assert getattr(test,'firstname') == 'John'
        assert getattr(test,'test', None) is None
        #print test._object_dict['test']
        assert getattr(test,'test',2) == 2

    def test_save_file(self):
        Test = MongoObject.factory('save_tests')
        id = Test.save_file('test')
        import gridfs
        fs = gridfs.GridFS(Test.__db__)
        assert fs.exists(id)
        print fs.get(id)
        assert fs.get(id).read() == 'test'

    def test_retrieve_file(self):
        Test = MongoObject.factory('fs_tests')
        id = Test.save_file('test')
        f = Test.retrieve_file(id)
        assert f.read() == 'test'

