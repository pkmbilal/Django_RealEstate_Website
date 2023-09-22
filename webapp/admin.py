from django.contrib import admin
from webapp.models import *

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_name', 'name_of_owner', 'building_type', 'number_of_rooms', 'mobile_number', 'current_lease_period')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'building_name', 'room_type', 'room_status', 'meter_number', 'account_number')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'mobile_number', 'id_type', 'id_number', 'building_name', 'room_number')

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('date','customer_name', 'room_number', 'amount', 'start_date', 'end_date', 'comment')

# Register your models here.
admin.site.register(BuildingType)
admin.site.register(RoomType)
admin.site.register(RoomStatus)
admin.site.register(IdType)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Receipt, ReceiptAdmin)