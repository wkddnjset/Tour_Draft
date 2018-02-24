from rest_framework import serializers
from _Item.models import Item

class ItemListSerializers(serializers.ModelSerializer):
    category_id = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = [
            'id',
            'category_id',
            'title',
            'subtitle',
            'content',
            'main_img',
            'sub_img_1',
            'sub_img_2',
            'sub_img_3',
            'address',
            'latitude',
            'longitude',
            'tel',
            'open_time',
            'close_time',
        ]