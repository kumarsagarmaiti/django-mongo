from .models import Student
from rest_framework_mongoengine import serializers


class StudentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Student
        fields = "__all__"


student_data = {"name": "Rita", "age": 22}

serialized_data=StudentSerializer(data=student_data)
if serialized_data.is_valid():
    serialized_data.save()