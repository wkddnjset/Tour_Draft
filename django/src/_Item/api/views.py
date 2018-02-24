from rest_framework import generics
from _Item.models import Item
from .serializers import ItemListSerializers

class ItemListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ItemListSerializers
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return Item.objects.all()