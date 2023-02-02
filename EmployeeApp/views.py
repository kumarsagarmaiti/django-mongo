# from rest_framework.generics import (
#     CreateAPIView,
#     ListAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from .serializers import GeneralSerializer
# from .models import Employee
# from django.shortcuts import get_object_or_404


# class EmployeeAdd(CreateAPIView):
#     GeneralSerializer.Meta.model = Employee
#     serializer_class = GeneralSerializer


# class GetEmployee(ListAPIView):
#     queryset = Employee.objects.all()
#     GeneralSerializer.Meta.model = Employee
#     serializer_class = GeneralSerializer


# class EmployeeDetail(RetrieveUpdateDestroyAPIView):
#     # queryset = Employee.objects.all()
#     # queryset=Employee.objects.get()
#     GeneralSerializer.Meta.model = Employee
#     serializer_class = GeneralSerializer
#     lookup_field = "employee_id"

#     def get_object(self):
#         employee_id = self.kwargs["employee_id"]
#         return Employee.objects.get(employee_id=employee_id)

#     # def get_queryset(self):
#     #     return Employee.objects.get(employee_id=self.kwargs["employee_id"])

#     # def perform_destroy(self, instance):
#     #     instance.delete()

#     def delete(self):
#         Employee.objects.delete(employee_id=self.kwargs["employee_id"])
#         # employee_doc = get_object_or_404(Employee, employee_id=self.kwargs["employee_id"])
#         # employee_doc.delete()
#         # return "success"


# from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from rest_framework import generics


class EmployeeAdd(generics.CreateAPIView):
    serializer_class = EmployeeSerializer


class EmployeeAll(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeOne(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    lookup_field = "employee_id"
    queryset = Employee.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(employee_id=self.kwargs[self.lookup_field])
        return obj

    def perform_destroy(self, instance):
        instance.delete()
    
    def perform_update(self, serializer):
        serializer.save()

# class EmployeeDetails(APIView):
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def get(self):
#         print('he')
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)

# class EmployeeInfo(RetrieveUpdateDestroyAPIView):
#     serializer_class=EmployeeSerializer
#     def get_object(self):
#         print('hell')

#         employee_id = self.kwargs["employee_id"]
#         return Employee.objects.get(employee_id=employee_id)
