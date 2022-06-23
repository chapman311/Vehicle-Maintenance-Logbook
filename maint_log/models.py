from pyexpat import model
from django.db import models
from django.forms import DateTimeField
from django.contrib.auth.models import User
import datetime

default_maintenance_intervals = """Tire Rotation: 5,000 miles

Oil Change: 7,500 miles or every year

Cabin Air Filter Replace: 30,000 miles or every 2 years

Engine Air Filter Replace: 30,000 miles or every 2 years

Transmission Fluid Replace: 30,000 miles or every 2 years

Differential Fluid Replace: 30,000 miles or every 2 years

Brake Fluid Replace: Every 3 years

Battery Replace: Every 5 years

Engine Coolant Replace: 60,000 or every 5 years

Spark Plugs: 100,000 miles

Timing Belt Replace: 100,000 miles"""


class Vehicle(models.Model):
    year = models.IntegerField(null=True)
    make = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    maintenance_intervals = models.TextField(default=default_maintenance_intervals, null=True)
        
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
    












