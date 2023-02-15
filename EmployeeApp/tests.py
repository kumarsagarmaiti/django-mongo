import unittest
from .models import Employee
import math
import requests


class EmployeeTest(unittest.TestCase):
    def test_employee_pagination(self):
        page_number = 1
        page_size = 5
        total_document_count = Employee.objects.count()
        range_of_pages = math.ceil(total_document_count / page_size)
        total_documents_found = 0
        for _ in range(range_of_pages):
            url = (
                f"http://127.0.0.1:8000/employees?page={page_number}&pageSize={page_size}"
            )
            response = requests.get(url)
            total_documents_found += len(response.json()["payload"]["data"])
            page_number += 1
        self.assertEqual(total_document_count, total_documents_found)

    def test_employee_pagination_retrieval(self):
        page_number = "page_number"
        page_size = "page_size"
        url = f"http://127.0.0.1:8000/employees?page={page_number}&pageSize={page_size}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 400)


# TODO: start the server from here and end after the test is done
