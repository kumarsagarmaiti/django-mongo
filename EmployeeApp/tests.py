import unittest
from mongoengine import connect
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPITestCase(unittest.TestCase):
    # connect("employee_db_django", host="mongodb://localhost:27017/")
    @classmethod
    def setUpClass(cls):
        pass

    employee1 = Employee(
        name="John Doe",
        email="johndoe@example.com",
        age=24,
        company="Google",
        gender="Male",
        password="password",
    )
    employee1.save()
    employee2 = Employee(
        name="Jane Doe",
        email="janedoe@example.com",
        age=26,
        company="Microsoft",
        gender="Female",
        password="password",
    )
    employee2.save()

    employee_data = {
        "name": "John Smith",
        "age": 27,
        "company": "Amazon",
        "gender": "Male",
        "email": "johnsmith@gmail.com",
        "password": "password",
    }
    employee_serializer = EmployeeSerializer(data=employee_data)

    def test_employee_serialization(self):
        self.assertTrue(self.employee_serializer.is_valid())

    def test_employee_created(self):
        try:
            if self.employee_serializer.is_valid():
                self.employee_serializer.create(self.employee_data)
            self.assertEqual(Employee.objects.count(), 3)
        except Exception as e:
            print(e)

    def test_employee_updated(self):
        self.employee1.update(set__name="John Doe Updated")
        self.assertEqual(
            Employee.objects.get(name="John Doe Updated").name, "John Doe Updated"
        )

    def test_employee_deleted(self):
        self.employee2.delete()
        self.assertEqual(Employee.objects.count(), 2)

    @classmethod
    def tearDownClass(cls):
        Employee.drop_collection()
