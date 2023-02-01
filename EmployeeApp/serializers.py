from rest_framework_mongoengine import serializers


class DepartmentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = "Department"
        fields = "__all__"
