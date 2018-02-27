from rest_framework import generics, serializers
from django.http import HttpResponse, JsonResponse
from ..models import TimeSlot, Address, Plan, Plan_Item
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

"""
PlanDetailAPIView

url : plans/plan_id
설명 : Plan models의 데이터를 plan_id를 이용하여 조회
HTTP METHOD : GET(조회), PUT(수정), DELETE(삭제)
"""
class PlanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlanDetailSerializer
    lookup_field = 'id'

    # Plan 조회
    def get_queryset(self, *args, **kwargs):
        query_set = Plan.objects.all()
        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Plan 수정
    def put(self, request, *args, **kwargs):
        serializer = PlanDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Plan 삭제
    def delete(self, *args, **kwargs):
        plan_id = self.kwargs['id']
        query_set = Plan.objects.all().filter(id=plan_id)
        query_set.delete()

"""
PlanCreateAPIView

url : plans
설명 : Plan models의 데이터를 등록
HTTP METHOD : POST
"""
class PlanCreateAPIView(generics.CreateAPIView):
    serializer_class = PlanCreateSerializer
    queryset = Plan.objects.all()

"""
SharePlanDetailAPIView

url : shareplans
설명 : Plan models의 share_flag가 true인 것을 조회 (공유해도 되는 것)
HTTP METHOD : GET
"""
class SharePlanDetailAPIView(generics.ListAPIView):
    queryset = Plan.objects.filter(share_flag=True)
    serializer_class = SharePlanDetailSerializer

"""
AddressDetailAPIView

url : addresses
설명 : Address models의 데이터 조회
HTTP METHOD : GET
"""
class AddressDetailAPIView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer

"""
TimeslotsDetailAPIView

url : timeslots
설명 : TimeSlot models의 데이터 조회
HTTP METHOD : GET
"""
class TimeslotsDetailAPIView(generics.ListAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotDetailSerializer

"""
UserPlanDetailAPIView

url : users/user_id/plans
설명 : Plan models의 데이터를 user_id를 이용하여 조회
HTTP METHOD : GET
"""
class UserPlanDetailAPIView(generics.ListAPIView):
    serializer_class = PlanDetailSerializer

    def get_queryset(self, *args, **kwargs):
        query_set = Plan.objects.filter(user_id=self.kwargs['user_id'])
        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

"""
PlanItemAPIView

url : plans/plan_id/items/item_id
설명 : Plan_Item models의 데이터를 plan_id,item_id를 이용하여 조회
HTTP METHOD : GET
"""
class PlanItemAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = PlanItemDetailSerializer
    lookup_field = 'plan_id'

    # Plan_Item plan_id, item_id를 이용하여 조회
    def get_queryset(self, *args, **kwargs):
        item_id = self.kwargs['item_id']
        query_set = Plan_Item.objects.filter(item_id=item_id)
        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

"""
PlanItemCreateAPIView

url : planitems
설명 : Plan_Item models의 데이터를 등록
HTTP METHOD : POST
"""
class PlanItemCreateAPIView(generics.CreateAPIView):
    serializer_class = PlanItemCreateSerializer
    queryset = Plan_Item.objects.all()