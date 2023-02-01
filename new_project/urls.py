from django.urls import path, include
from rest_framework import routers  # Ensure nested routers are imported
from EmployeeApp.views import create_department

urlpatterns = [
    path('register',create_department)
]