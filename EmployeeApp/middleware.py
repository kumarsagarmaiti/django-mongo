import logging

from mongoengine import DoesNotExist
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission

from .models import Employee

EXCLUDED_URLS = ["/register", "/employees", "/add-person","/login"]


class EmployeeAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if request.path in EXCLUDED_URLS:
            return None, None

        email = request.META.get("HTTP_EMAIL")
        password = request.META.get("HTTP_PASSWORD")
        if not email or not password:
            raise exceptions.AuthenticationFailed(
                "Email and password required in headers"
            )
        try:
            user = Employee.objects.get(email=email, password=password)
            print(user)
        except DoesNotExist:
            raise exceptions.AuthenticationFailed("Incorrect email or password")

        return None, None


class EmployeeAuthorisation(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.path in EXCLUDED_URLS:
                return None, None
            email = request.META.get("HTTP_EMAIL")
            password = request.META.get("HTTP_PASSWORD")
            employee = Employee.objects.get(
                email=email, password=password, pk=view.kwargs.get("pk")
            )
            if employee:
                return None, None
        except DoesNotExist:
            raise exceptions.NotAuthenticated("Authorisation fail")


logging.basicConfig(filename="middleware_logs.txt", filemode="a", level=logging.INFO)


class EmployeeLogger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.info(f"Started request: {request.method} {request.path}")
        response = self.get_response(request)
        logging.info(
            f"Finished request: {request.method} {request.path} with status {response.status_code}"
        )
        return response
