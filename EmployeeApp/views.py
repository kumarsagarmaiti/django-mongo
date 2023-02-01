from rest_framework.generics import CreateAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.mixins import CreateModelMixin,ListModelMixin


class StudentView(CreateAPIView, CreateModelMixin,ListModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        student=get_object_or_404