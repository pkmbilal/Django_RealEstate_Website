from django.db import models

# Create your models here.
class BuildingType(models.Model):
    building_type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Building Type'

    def __str__(self):
        return self.building_type

class RoomType(models.Model):
    room_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Room Type'
    
    def __str__ (self):
        return self.room_type

class RoomStatus(models.Model):
    room_status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Room Status'

    def __str__ (self):
        return self.room_status

class Building(models.Model):
    building_name = models.CharField(max_length=50)
    name_of_owner = models.CharField(max_length=50)
    building_type = models.ForeignKey(BuildingType, on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField()
    mobile_number = models.IntegerField()
    current_lease_period = models.DateField()

    class Meta:
        verbose_name_plural = 'Buildings'

    def __str__ (self):
        return self.building_name

class Room(models.Model):
    room_number = models.IntegerField()
    building_name = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.DO_NOTHING)
    meter_number = models.CharField(max_length=16)
    account_number = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__ (self):
        return str(self.room_number)