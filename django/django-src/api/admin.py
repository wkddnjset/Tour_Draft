from django.contrib import admin
from .models import BlogPost, image
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(image)