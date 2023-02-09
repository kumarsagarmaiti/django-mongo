from mongoengine import Document,StringField

class Person(Document):
    fName=StringField()
    lName=StringField()
    
    