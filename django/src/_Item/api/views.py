from rest_framework import generics
from ..models import *
from .serializers import *

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


class DistanceListView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = DistanceSerializers

    def get_queryset(self):
        return Distance.objects.all()


class DistanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DistanceSerializers

    def get_queryset(self):
        return Distance.objects.all()

