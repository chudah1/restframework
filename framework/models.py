from django.db import models
import rest_framework


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=250)
    position=models.CharField(max_length=250)
    age=models.IntegerField(default=23)
    date_emp=models.DateTimeField()

    def __str__(self):
        return self.name
