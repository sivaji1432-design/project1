from rest_framework import serializers
from app1.models import Employee,Book

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'