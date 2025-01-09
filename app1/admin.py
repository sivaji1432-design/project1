from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    emp_data = ['eid','ename','esal']
admin.site.register(Employee,EmployeeAdmin)