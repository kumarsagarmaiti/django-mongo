from rest_framework.generics import CreateAPIView
from .serializers import GeneralSerializer
from .models import Employee


class EmployeeAdd(CreateAPIView):
    GeneralSerializer.Meta.model=Employee
    serializer_class=GeneralSerializer