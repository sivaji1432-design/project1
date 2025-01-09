from django.shortcuts import render
from app1.serializer import EmployeeSerializers
from app1.models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class EmpView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class =  EmployeeSerializers