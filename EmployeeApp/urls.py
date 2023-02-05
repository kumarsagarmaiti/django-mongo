from django.urls import path
from .views import EmployeeAdd, EmployeeAll, EmployeeOne

urlpatterns = [
    path("register", EmployeeAdd.as_view()),
    path("employees", EmployeeAll.as_view()),
    path("employee/<int:pk>", EmployeeOne.as_view()),
]
