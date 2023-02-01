from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import GeneralSerializer
from .models import Employee


class EmployeeAdd(CreateAPIView):
    GeneralSerializer.Meta.model = Employee
    serializer_class = GeneralSerializer


class GetEmployee(ListAPIView):
    queryset = Employee.objects.all()
    GeneralSerializer.Meta.model = Employee
    serializer_class = GeneralSerializer


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    # queryset = Employee.objects.all()
    # queryset=Employee.objects.get()
    GeneralSerializer.Meta.model = Employee
    serializer_class = GeneralSerializer

    def get_object(self):
        print(self.request)
        # employee_id = self.request.employee_id
        # return Employee.objects.get(employee_id=employee_id)
