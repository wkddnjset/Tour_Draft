from django.contrib import admin
<<<<<<< HEAD
from .models import ( Item, Tag, Item_Tag )
=======
from .models import *
>>>>>>> 77f9ab06c6220164bdd2d072a5a630e38d40069d
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