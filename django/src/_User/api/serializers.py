from rest_framework import serializers
from ..models import *
from django.core.validators import ValidationError
from django.db.models import Q
from django.core import validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'age',
            'sex',
        ]


class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'item_id',
            'user_id',
            'star_point',
            'comment',
        ]

    def update(self, instance, validated_data):
        item_id = validated_data['item_id']
        user_id = validated_data['user_id']
        star_point = validated_data['star_point']
        comment = validated_data['comment']

        review_obj = Review(
            item_id=item_id,
            user_id=user_id,
            star_point=star_point,
            comment=comment,
        )

        review_obj.save()
        return validated_data

    def create(self, validated_data):
        item_id = validated_data['item_id']
        user_id = validated_data['user_id']
        star_point = validated_data['star_point']
        comment = validated_data['comment']

        review_obj = Review(
            item_id=item_id,
            user_id=user_id,
            star_point=star_point,
            comment=comment,
        )

        review_obj.save()
        return validated_data


class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = [
            'id',
            'item_id',
            'user_id',
        ]

    def update(self, instance, validated_data):
        item_id = validated_data['item_id']
        user_id = validated_data['user_id']

        pick_obj = Pick(
            item_id=item_id,
            user_id=user_id,
        )

        pick_obj.save()
        return validated_data

    def create(self, validated_data):
        item_id = validated_data['item_id']
        user_id = validated_data['user_id']

        pick_obj = Pick(
            item_id=item_id,
            user_id=user_id,
        )

        pick_obj.save()
        return validated_data