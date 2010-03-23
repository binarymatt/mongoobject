from pymongo import Connection
from pymongo.objectid import ObjectId

class Document(object):
    def __init__(self, object_dict):
        self.__dict__['_object_dict'] = object_dict
    
    def save(self):
        return self.__db__[self.__collection__].save(self._object_dict, safe=True)

    def delete(self):
        object_id = self._object_dict['_id']
        if object_id:
            self.__db__[self.__collection__].remove(object_id)
            del self._object_dict['_id']
            return True
        return False
    
    def __getattr__(self, name):
        return self._object_dict[name]
    
    def __setattr__(self, name, value):
        if name is not '_id':
            self._object_dict[name] = value
    
    def __setitem__(self, name, value):
        self.__setattr__(name, value)
    
    @classmethod
    def create(cls, dictionary):
        object_id = cls.__db__[cls.__collection__].insert(dictionary)
        #dictionary['_id'] = str(object_id)
        return cls(dictionary)
    
    @classmethod
    def get(cls, object_id):
        object_dict = cls.__db__[cls.__collection__].find_one({'_id':ObjectId(object_id)})
        return cls(object_dict)
    
    @classmethod
    def find(cls, spec=None):
        for object_dict in cls.__db__[cls.__collection__].find(spec=spec):
            yield cls(object_dict)

class MongoObject(object):
    
    @classmethod
    def connection(cls, host='localhost', port=27017):
        if not hasattr(cls, '_connection'):
            cls._connection = Connection(host, port)
        return cls._connection
    
    @classmethod
    def db(cls, db_name='mongo_object'):
        return cls.connection()[db_name]
    
    @classmethod
    def factory(cls, collection_name, db_name='mongo_object'):
        items = {'__collection__': collection_name}
        items['__db__'] = cls.db()
        Klass = type(collection_name.capitalize(),(Document,), items)
        return Klass