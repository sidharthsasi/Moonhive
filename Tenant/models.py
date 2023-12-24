from django.db import models
from Account.models import *
# Create your models here.



class Property(models.Model):

    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()




CHOICES = [('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')]

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=50, choices=CHOICES)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.property.name} - {self.unit_type}"
    



class Tenant(models.Model):
    unit = models.OneToOneField(Unit, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    monthly_rent_date = models.DateField()
    expiry_date = models.DateField()
    document_proof = models.FileField(upload_to='proof/',null=True, blank=True)
    def __str__(self):
        return self.name


