from django.contrib import admin
from webapp.models import BuildingType, RoomStatus, RoomType, Building, Room

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_name', 'name_of_owner', 'building_type', 'number_of_rooms', 'mobile_number', 'current_lease_period')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'building_name', 'room_type', 'room_status', 'meter_number', 'account_number')

# Register your models here.
admin.site.register(BuildingType)
admin.site.register(RoomType)
admin.site.register(RoomStatus)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)