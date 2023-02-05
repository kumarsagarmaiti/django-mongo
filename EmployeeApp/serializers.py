from rest_framework_mongoengine import serializers
from .models import Employee
class EmployeeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
