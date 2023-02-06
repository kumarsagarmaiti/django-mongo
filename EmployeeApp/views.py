from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from rest_framework_mongoengine import generics
import logging
from rest_framework.exceptions import ValidationError, NotFound
from mongoengine import DoesNotExist
import time

logging.basicConfig(filename="logs.txt", filemode="a", level=logging.INFO)


class EmployeeAdd(generics.CreateAPIView):
    try:
        serializer_class = EmployeeSerializer
        logging.info(f"Document created successfully at {time.ctime()}")

    except ValidationError as e:
        Response(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        Response(f"An error occurred while creating the document")


class EmployeeAll(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        if "name" in params:
            queryset = queryset.filter(name=params["name"])
        if "age" in params:
            queryset = queryset.filter(age=params["age"])
        return queryset


class EmployeeOne(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    lookup_field = "pk"
    queryset = Employee.objects.all()

    def get_queryset(self):
        queryset = Employee.objects.get(pk=self.kwargs[self.lookup_field])
        return queryset

    def get_object(self):
        try:
            queryset = self.get_queryset()
            if queryset == None:
                raise Employee.DoesNotExist
            # obj = queryset.get(pk=self.kwargs[self.lookup_field])
            # return obj
            return queryset
        except Employee.DoesNotExist:
            return NotFound(detail="The document doesn't exist")
        except Exception as e:
            logging.error(
                f"Failed to retrieve document with the ID {self.kwargs[self.lookup_field]}"
            )
            return Response(
                {"detail": "An error occurred while processing your request."}, status=500
            )

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            logging.info(
                f"Successfully updated document with ID {kwargs[self.lookup_field]}"
            )
            return response
        except ValidationError as e:
            logging.error(
                f"Failed to update document with ID {kwargs[self.lookup_field]} due to validation error: {e}"
            )
            return Response({"detail": e.detail}, status=e.status_code)
        except DoesNotExist:
            return Response({"detail": "Document not found."}, status=404)
        except Exception as e:
            logging.error(
                f"Failed to update document with ID {kwargs[self.lookup_field]} due to an error: {e}"
            )
            return Response(
                {"detail": "An error occurred while processing your request."}, status=500
            )

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            logging.info(
                f"Successfully deleted document with ID {kwargs[self.lookup_field]}"
            )
            return Response(
                f"Successfully deleted document with ID {kwargs[self.lookup_field]}"
            )
        except DoesNotExist:
            return Response({"detail": "Document not found."}, status=404)
        except Exception as e:
            logging.error(
                f"Failed to delete document with ID {kwargs[self.lookup_field]} due to an error: {e}"
            )
            return Response(
                {"detail": "An error occurred while processing your request."}, status=500
            )
