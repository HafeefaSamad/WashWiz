from django.db import models

# Create your models here.

class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=20)

    def __str__(self):
        return self.vehicle_type
    
class Package(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Variation(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    Package = models.ForeignKey(Package, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vehicle_type}, {self.Package}"
    