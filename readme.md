MongoObject
===========

About
-----
MongoObject is a simple object mapper for mongo database documents.

Installation
------------
pip install mongoobject

Dependencies
------------
pymongo 1.5.1

Usage
-----

    Contact = MongoObject.factory(collection_name='contacts', db_name='contact_db')
    
    #create a new document
    contact = Contact.create({'first_name': 'John','last_name':'Doe','email':'jdoe@acme.com'})
    
    #access attributes
    contact.first_name
    
    #query for documents
    contacts = Contact.find({'first_name':'John'})
    
    #get a single contact
    contact = Contact.get(object_id=1234)
    
    #save changes to a contact
    contact.first_name = 'Jane'
    contact.new_attribute = 6
    contact.save() # saves both the old attribute and also adds a new attribute to the document


