from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'age', 'sex']


admin.site.register(User, UserAdmin)


class PickAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','item_id')


admin.site.register(Pick, PickAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'user_id', 'star_point', 'comment')


admin.site.register(Review, ReviewAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)