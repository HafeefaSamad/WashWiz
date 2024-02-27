from django.db import models
from apps.accounts.models import Account

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class VehicleType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20)

    def __str__(self):
        return self.vehicle_type
    
class Package(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Variation(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vehicle_type}, {self.package}"
    

class Slot(models.Model):
    TIMESLOT_CHOICES = (
        (0, '9-10'),
        (1, '10-11'),
        (2, '11-12'),
        (3, '12-1'),
        (4, '2-3'),
        (5, '3-4'),
        (6, '4-5'),
    )

    date = models.DateField(null=True, blank=True)
    timeslot = models.IntegerField(choices=TIMESLOT_CHOICES, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_timeslot_display()}, {self.date}"
    