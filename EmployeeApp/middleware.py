from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from .models import Employee


class MongoEngineAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if (
            request.META.get("REQUEST_METHOD") == "POST"
            and request.META.get("PATH_INFO") == "/register"
        ):
            return (None, None)

        email = request.META.get("HTTP_EMAIL")
        password = request.META.get("HTTP_PASSWORD")
        if not email or not password:
            raise exceptions.AuthenticationFailed(
                "Email and password required in headers"
            )
        try:
            user = Employee.objects.get(email=email, password=password)
        except Employee.DoesNotExist:
            raise exceptions.AuthenticationFailed("Incorrect email or password")

        return (None, None)
