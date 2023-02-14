import unittest
from .models import Employee
from .serializers import EmployeeSerializer
import math
import requests

# class EmployeeAPITestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         pass
#     employee1 = Employee(
#         name="John Doe",
#         email="johndoe@example.com",
#         age=24,
#         company="Google",
#         gender="Male",
#         password="password",
#     )
#     employee1.save()
#     employee2 = Employee(
#         name="Jane Doe",
#         email="janedoe@example.com",
#         age=26,
#         company="Microsoft",
#         gender="Female",
#         password="password",
#     )
#     employee2.save()

#     employee_data = {
#         "name": "John Smith",
#         "age": 27,
#         "company": "Amazon",
#         "gender": "Male",
#         "email": "johnsmith@gmail.com",
#         "password": "password",
#     }
#     employee_serializer = EmployeeSerializer(data=employee_data)

#     def test_employee_serialization(self):
#         self.assertTrue(self.employee_serializer.is_valid())

#     def test_employee_created(self):
#         try:
#             if self.employee_serializer.is_valid():
#                 self.employee_serializer.create(self.employee_data)
#             self.assertEqual(Employee.objects.count(), 3)
#         except Exception as e:
#             print(e)

#     def test_employee_updated(self):
#         self.employee1.update(set__name="John Doe Updated")
#         self.assertEqual(
#             Employee.objects.get(name="John Doe Updated").name, "John Doe Updated"
#         )

#     def test_employee_deleted(self):
#         self.employee2.delete()
#         self.assertEqual(Employee.objects.count(), 2)

#     @classmethod
#     def tearDownClass(cls):
#         Employee.drop_collection()


class EmployeeTest(unittest.TestCase):
    def test_employee_pagination(self):
        page_number = 1
        page_size = 5
        total_document_count = Employee.objects.count()
        range_of_pages = math.ceil(total_document_count / page_size)
        total_documents_found = 0
        for i in range(range_of_pages):
            url = (
                f"http://127.0.0.1:8000/employees?page={page_number}&pageSize={page_size}"
            )
            response = requests.get(url)
            total_documents_found += len(response.json()["payload"]["data"])
            page_number += 1
        self.assertEqual(total_document_count, total_documents_found)
