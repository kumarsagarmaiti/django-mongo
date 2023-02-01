from mongoengine import (
    Document,
    fields,
)


# Create your models here.
class Department(Document):
    name = fields.StringField(required=True)
    company = fields.StringField(required=True)
    address = fields.StringField(required=True)


class Employee(Document):
    first_name = fields.StringField(required=True)
    last_name = fields.StringField(required=True)
    age = fields.IntField(required=True)
