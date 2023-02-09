from django.urls import path

from .views import EmployeeAdd, EmployeeAll, EmployeeOne, EmployeeLogin 

urlpatterns = [
    path("register", EmployeeAdd.as_view()),
    path("employees", EmployeeAll.as_view()),
    path("employee/<int:pk>", EmployeeOne.as_view()),
    path("login",EmployeeLogin.as_view())
]
