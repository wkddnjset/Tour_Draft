from .views import *
from django.conf.urls import url
# from django.urls import path
# from . import views

app_name='_Plan'

urlpatterns = [
    # 각 user에 맞는 plan 데이터
    url(r'^users/(?P<user_id>\d+)/plans/', UserPlanDetailAPIView.as_view(), name='user_plans'),

    # 공유되는 plan 조회
    url(r'^shareplans/', SharePlanDetailAPIView.as_view(), name='share_plans'),

    # 모든 plan 조회 / 수정 / 삭제
    url(r'^plans/(?P<id>\d+)/$', PlanDetailAPIView.as_view(), name='plans'),

    # plan 등록
    url(r'^plans/$', PlanCreateAPIView.as_view(), name='plans'),

    # 모든 address 조회
    url(r'^addresses/', AddressDetailAPIView.as_view(),name='addresses'),

    # 모든 timeslot 조회
    url(r'^timeslots/', TimeslotsDetailAPIView.as_view(),name='timeslots'),

    # planitem 등록
    url(r'^planitems/', PlanItemCreateAPIView.as_view(),name='create_planitems'),

    # 모든 planitem 조회
    url(r'^planitems/(?P<plan_id>\d+)/items/(?P<item_id>\d+)/$', PlanItemAPIView.as_view(),name='plansitems')
]

