from rest_framework_mongoengine import serializers


class EmployeeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = None
        fields = "__all__"
