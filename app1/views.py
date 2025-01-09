from django.shortcuts import render
from app1.serializer import EmployeeSerializers
from app1.models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class EmpView(APIView):
    def get(self,request):
        instance=Employee.objects.all()
        serializer = EmployeeSerializers(instance,many=True)
        return Response(serializer.data)