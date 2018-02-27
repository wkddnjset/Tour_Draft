from rest_framework import serializers
from ..models import *
from django.core.validators import ValidationError
from django.db.models import Q
from django.core import validators

class PlanDetailSerializer(serializers.ModelSerializer):

    # Plan Data 조회
    class Meta:
        model = Plan
        fields = [
            'user_id',
            'plan_name',
            'share_flag',
            'start_datetime',
            'start_address_id',
            'end_datetime',
            'end_address_id'
        ]

class PlanCreateSerializer(serializers.ModelSerializer):

    # Plan Data 조회
    class Meta:
        model = Plan
        fields = [
            'user_id',
            'plan_name',
            'share_flag',
            'start_datetime',
            'start_address_id',
            'end_datetime',
            'end_address_id'
        ]

    # Plan 등록
    def create(self, validated_data):
        user_id             = validated_data['user_id']
        plan_name           = validated_data['plan_name']
        share_flag          = validated_data['share_flag']
        start_datetime      = validated_data['start_datetime']
        start_address_id    = validated_data['start_address_id']
        end_datetime        = validated_data['end_datetime']
        end_address_id      = validated_data['end_address_id']

        plan_obj = Plan(
            user_id             = user_id,
            plan_name           = plan_name,
            share_flag          = share_flag,
            start_datetime      = start_datetime,
            start_address_id    = start_address_id,
            end_datetime        = end_datetime,
            end_address_id      = end_address_id
        )

        plan_obj.save()

        return validated_data

class SharePlanDetailSerializer(serializers.ModelSerializer):

    # Share Plan Data 조회
    class Meta:
        model = Plan
        fields = [
            'user_id',
            'plan_name',
            'share_flag',
            'start_datetime',
            'start_address_id',
            'end_datetime',
            'end_address_id'
        ]

class AddressDetailSerializer(serializers.ModelSerializer):

    # Address Data 조회
    class Meta:
        model = Address
        fields = [
            'location_name',
            'address',
            'latitude',
            'longitude'
        ]

class TimeSlotDetailSerializer(serializers.ModelSerializer):

    # TimeSlot Data 조회
    class Meta:
        model = TimeSlot
        fields = [
            'start_time',
            'end_time'
        ]


class PlanItemCreateSerializer(serializers.ModelSerializer):

    # TimeSlot Data 조회
    class Meta:
        model = Plan_Item
        fields = [
            'plan_id',
            'item_id',
            'timeslot_id',
            'day'
        ]

    def create(self, validated_data):
        plan_id             = validated_data['plan_id']
        item_id             = validated_data['item_id']
        timeslot_id         = validated_data['timeslot_id']
        day                 = validated_data['day']

        if not plan_id and not item_id:
            raise ValidationError("A plan_id and item_id must be required to login")

        plan_item_obj = Plan_Item(
            plan_id         = plan_id,
            item_id         = item_id,
            timeslot_id     = timeslot_id,
            day             = day
        )

        plan_item_obj.save()

        return validated_data


class PlanItemDetailSerializer(serializers.ModelSerializer):

    # TimeSlot Data 조회
    class Meta:
        model = Plan_Item
        fields = [
            'plan_id',
            'item_id',
            'timeslot_id',
            'day'
        ]