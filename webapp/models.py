from django.db import models

# Create your models here.
class BuildingType(models.Model):
   building_type = models.CharField(max_length=100)

   def __str__(self):
       return self.building_type

class Building(models.Model):
    building_name = models.CharField(max_length=50)
    name_of_owner = models.CharField(max_length=50)
    building_type = models.ForeignKey(BuildingType, on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField()
    mobile_number = models.IntegerField()
    current_lease_period = models.DateField()