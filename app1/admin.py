from django.contrib import admin
from app1.models import Employee,Book
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    emp_data = ['eid','ename','esal']
class BookAdmin(admin.ModelAdmin):
    boo_data = ['bid','bname','bprice']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Book,BookAdmin)