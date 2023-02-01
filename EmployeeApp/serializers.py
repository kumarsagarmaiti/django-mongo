from .models import Employee
from rest_framework_mongoengine import serializers


# class EmployeeSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Employee
#         fields = "__all__"


class GeneralSerializer(serializers.DocumentSerializer):
    class Meta:
        model = None
        fields = "__all__"


# student_data = {"name": "Rita", "age": 22}

# serialized_data=StudentSerializer(data=student_data)
# if serialized_data.is_valid():
#     serialized_data.save()
