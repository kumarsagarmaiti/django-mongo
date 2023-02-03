# challenge/urls.py
from django.urls import path

# from .views import EmployeeAdd, GetEmployee, EmployeeDetail
from .views import EmployeeAdd, EmployeeAll,EmployeeOne

# urlpatterns = [
#     path("add-employee", EmployeeAdd.as_view()),
#     path("get-employee", GetEmployee.as_view()),
#     path("get-employee/<int:employee_id>", EmployeeDetail.as_view()),
# ]

urlpatterns = [
    path("register", EmployeeAdd.as_view()),
    path("employees", EmployeeAll.as_view()),
    path("employee/<int:pk>", EmployeeOne.as_view()),
]
