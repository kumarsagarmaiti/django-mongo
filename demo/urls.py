from django.urls import path
from .views import create_person

urlpatterns=[
    path("add-person",create_person.as_view())
]