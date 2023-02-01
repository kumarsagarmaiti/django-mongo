from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .serializers import DepartmentSerializer
from rest_framework.parsers import JSONParser


@api_view(["POST"])
def create_department(request):
    print(request.data)
    # department_data = JSONParser().parse(request.data)
    # department_serializer = DepartmentSerializer(data=department_data)
    # if department_serializer.is_valid():
    #     department_serializer.save()
    #     return JsonResponse(department_serializer.data)
    # return JsonResponse(department_serializer.errors)
