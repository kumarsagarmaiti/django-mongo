from mongoengine import Document, SequenceField, StringField, IntField, EmailField
from enum import Enum
from rest_framework.exceptions import ValidationError


class GenderEnums(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [item.value for item in cls]


class Employee(Document):
    employee_id = SequenceField(required=False, primary_key=True)
    name = StringField(required=True, max_length=50)
    age = IntField(required=True, min_value=18, max_value=50)
    company = StringField(required=True, max_length=50)
    gender = StringField(choices=GenderEnums.choices(), default=GenderEnums.OTHER)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

    def clean(self):
        if self.gender == GenderEnums.MALE.value and self.age > 30:
            raise ValidationError("For male employees, age should be under 31")
        elif self.gender == GenderEnums.FEMALE.value and self.age < 20:
            raise ValidationError("For female employees, age should be above 20")
