from rest_framework import serializers
from _Item.models import Item, Distance

class ItemListSerializers(serializers.ModelSerializer):
    category_id = serializers.StringRelatedField()
    main_img = serializers.ImageField(use_url=True)
    sub_img_1 = serializers.ImageField(use_url=True)
    sub_img_2 = serializers.ImageField(use_url=True)
    sub_img_3 = serializers.ImageField(use_url=True)

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


class DistanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = [
            'id',
            'src',
            'dst',
            'distance',
        ]

    def create(self, validated_data):
        src = validated_data['src']
        dst = validated_data['dst']
        distance = validated_data['distance']

        distance_obj = Distance(
            src=src,
            dst=dst,
            distance=distance,
        )

        distance_obj.save()
        return validated_data
