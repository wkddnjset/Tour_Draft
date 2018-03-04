from rest_framework import generics
from ..models import Item
from .serializers import ItemListSerializers

class ItemListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ItemListSerializers

    def get_queryset(self):
        return Item.objects.all()

class ItemDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ItemListSerializers

    def get_queryset(self):
        return Item.objects.all()