from rest_framework import generics, serializers
from ..models import TimeSlot, Address, Plan, Plan_Item
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

# Plan 조회의 경우 plan_id를 이용해서 조회 (즉 plan models의 pk)
class PlanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlanDetailSerializer

    # Plan 조회
    def get(self, *args, **kwargs):
        id = self.kwargs['id']
        query_set = Plan.objects.filter(id=id)

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

# Plan 등록
class PlanCreateAPIView(generics.CreateAPIView):
    serializer_class = PlanCreateSerializer

    def post(self, request):
        data = request.data
        serializer = PlanCreateSerializer(data=data)
        query_set = Plan.objects.filter(user_id=data.user_id)

# Plan 조회의 경우 share_flag를 이용하여 조회 (수정 필요)
class SharePlanDetailAPIView(generics.ListAPIView):

    queryset = Plan.objects.filter(share_flag=1)
    serializer_class = SharePlanDetailSerializer

# Address 전체 조회의 경우 pk에 관계 없이 전체 조회 (수정 필요)
class AddressDetailAPIView(generics.ListAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer

# TimeSlot 전체 조회의 경우 pk에 관계 없이 전체 조회 (수정 필요)
class TimeslotsDetailAPIView(generics.ListAPIView):

    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotDetailSerializer

# Plan user_id를 이용하여 조회 (수정 필요)
class UserPlanDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = PlanDetailSerializer

    def get(self, *args, **kwargs):
        user_id = self.kwargs['user_id']
        query_set = Plan.objects.all().filter(user_id=user_id)

        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# plan_item 조회의 경우 plan_id, item_id를 이용하여 조회 (수정 필요)
class PlanItemAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = PlanItemDetailSerializer

    # Plan_Item plan_id, item_id를 이용하여 조회
    def get(self, *args, **kwargs):
        plan_id = self.kwargs['plan_id']
        item_id = self.kwargs['item_id']

        query_set = Plan_Item.objects.filter(plan_id=plan_id, item_id=item_id)

        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Plan Item 등록 API
class PlanItemCreateAPIView(generics.CreateAPIView):
    serializer_class = PlanItemCreateSerializer

    # Plan_Item 등록
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PlanItemCreateSerializer(data=data)
        query_set = Plan_Item.objects.filter(plan_id=data.plan_id, item_id=data.item_id)