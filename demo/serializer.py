from rest_framework_mongoengine import serializers

from .models import Person


class PersonSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Person
        fields = "__all__"
