from rest_framework_mongoengine import generics
from .serializer import PersonSerializer
from any_case import converts_keys


class create_person(generics.CreateAPIView):
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        converts_keys(request.data, case="camel", inplace=True)
        print(request.data)
        return super().post(request, *args, **kwargs)
