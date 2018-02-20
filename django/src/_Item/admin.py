from django.contrib import admin
from .models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'title', 'latitude', 'longitude', 'tel')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')

class Item_TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'tag_id')

admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Item_Tag, Item_TagAdmin)