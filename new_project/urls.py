from django.urls import path, include

urlpatterns = [path("", include("EmployeeApp.urls")), path("", include("demo.urls"))]
