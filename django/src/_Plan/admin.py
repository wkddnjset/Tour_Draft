from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
from .models import Item
from .models import TimeSlot
from .models import Address
from .models import Plan
from .models import Plan_Item
=======
from .models import *
>>>>>>> 77f9ab06c6220164bdd2d072a5a630e38d40069d

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
=======

# Register your models here.
>>>>>>> 206a777a6d2c7dacce5d156d933cc8fbe5bfc195
