from django.db import models

# Create your models here.
class Employee(models.Model):
    eid  = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=40)
    esal = models.FloatField(default=None)
    def __str__(self):
        return self.ename