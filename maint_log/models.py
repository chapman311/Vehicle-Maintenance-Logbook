from pyexpat import model
from django.db import models
from django.forms import DateTimeField
from django.contrib.auth.models import User
import datetime


class Vehicle(models.Model):
    year = models.IntegerField(null=True)
    make = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return f'{self.year}, {self.make}, {self.model}, {self.user}'
    
    
class MaintenanceItem(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateField('date completed', null=True)
    mileage = models.IntegerField(null=True)
    notes = models.CharField(max_length=300, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.name}, {self.date}, {self.vehicle}'












