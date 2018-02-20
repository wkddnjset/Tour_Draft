from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id']

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time')

admin.site.register(TimeSlot, TimeSlotAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'location_name', 'address', 'latitude', 'longitude')

admin.site.register(Address, AddressAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'share_flag', 'start_datetime', 'start_address_id', 'end_datetime', 'end_address_id')

admin.site.register(Plan, PlanAdmin)

class Plan_ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'itemslot_id', 'day')

admin.site.register(Plan_Item, Plan_ItemAdmin)