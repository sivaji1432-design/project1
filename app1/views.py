from django.shortcuts import render
from app1.serializer import EmployeeSerializers,BookSerializers
from app1.models import Employee,Book
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from rest_framework.settings import api_settings
# Create your views here.
class EmpView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class =  EmployeeSerializers

class BaseView(ViewSet):
    def create(self,request,**hints):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        headers=self.get_headers(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)
    def get_headers(self,data):
        try:
            return {'LOCATION':str(data[api_settings.URL_FIELD_NAME])}
        except:
            return {}
    def list(self,request):
        instance = Book.objects.all()
        serializer = BookSerializers(instance,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        try:
            instance = Book.objects.get(bid=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = BookSerializers(instance)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def update(self,request,pk=None,**kwargs):
        partial = kwargs.pop('partial',False)
        try:
            instance=Book.objects.get(bid=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = BookSerializers(instance,data=request.data,partial=partial)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        if getattr(instance,'_prefetced_objects_cache',None):
            instance._prefetched_objects_cache
        return Response(serializer.data)
    def partial_update(self,request,pk=None,**kwargs):
        partial = kwargs.pop('partial',True)
        try:
            instance=Book.objects.get(bid=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = BookSerializers(instance,data=request.data,partial=partial)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        if getattr(instance,'_prefetced_objects_cache',None):
            instance._prefetched_objects_cache
        return Response(serializer.data)
    
    def destroy(self,request,pk=None):
        try:
            instance=Book.objects.get(bid=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            self.perform_delete(instance)
        return Response(status=status.HTTP_200_OK)
            
    def perform_delete(self,instance):
        instance.delete()
        
