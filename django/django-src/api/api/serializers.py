from rest_framework import serializers
from api.models import BlogPost

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
        ]