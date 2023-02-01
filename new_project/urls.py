from django.urls import path, include
from EmployeeApp import views

urlpatterns = [path("register", views.ArticleViewSet.as_view())]
