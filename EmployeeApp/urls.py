# challenge/urls.py
from django.urls import path
from .views import EmployeeAdd

urlpatterns = [path("add-employee", EmployeeAdd.as_view())]
