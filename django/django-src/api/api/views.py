from rest_framework import generics
from api.models import BlogPost
from .serializers import BlogPostSerializers

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializers
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()