from django.contrib import admin
from .models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'title', 'latitude', 'longitude', 'tel')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')

class Item_TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'tag_id')

class DistanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'src', 'dst', 'distance')


admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Item_Tag, Item_TagAdmin)
admin.site.register(Distance, DistanceAdmin)