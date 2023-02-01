# challenge/urls.py
from django.urls import path
from .views import EmployeeAdd, GetEmployee, EmployeeDetail

urlpatterns = [
    path("add-employee", EmployeeAdd.as_view()),
    path("get-employee", GetEmployee.as_view()),
    path("get-employee/<int:employee_id>", EmployeeDetail.as_view()),
]
