from rest_framework.generics import CreateAPIView
from .serializers import EmployeeSerializer


class EmployeeAdd(CreateAPIView):
    serializer_class=EmployeeSerializer