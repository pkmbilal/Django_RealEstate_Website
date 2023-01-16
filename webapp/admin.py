from django.contrib import admin
from webapp.models import BuildingType, Building

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_name', 'name_of_owner', 'building_type', 'number_of_rooms', 'mobile_number', 'current_lease_period')

# Register your models here.
admin.site.register(BuildingType)
admin.site.register(Building, BuildingAdmin)