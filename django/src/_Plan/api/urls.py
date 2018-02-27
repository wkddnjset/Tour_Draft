from .views import *
from django.conf.urls import url
# from django.urls import path
# from . import views

app_name='_Plan'

urlpatterns = [
    # 각 user_id에 맞는 Plan models의 데이터 조회
    url(r'^users/(?P<user_id>\d+)/plans/', UserPlanDetailAPIView.as_view(), name='user_plans'),

    # 공유할 수 있는 Plan 데이터 조회
    url(r'^shareplans/', SharePlanDetailAPIView.as_view(), name='share_plans'),

    # 모든 Plan models의 데이터 조회 / 수정 / 삭제
    url(r'^plans/(?P<id>\d+)/$', PlanDetailAPIView.as_view(), name='plans'),

    # Plan models에 데이터 등록
    url(r'^plans/$', PlanCreateAPIView.as_view(), name='plans'),

    # 모든 Address 조회
    url(r'^addresses/', AddressDetailAPIView.as_view(),name='addresses'),

    # 모든 TimeSlot 조회
    url(r'^timeslots/', TimeslotsDetailAPIView.as_view(),name='timeslots'),

    # Plan_Item models에 데이터 등록
    url(r'^planitems/', PlanItemCreateAPIView.as_view(),name='create_planitems'),

    # 모든 Plan_Item 조회
    url(r'^plans/(?P<plan_id>\d+)/items/(?P<item_id>\d+)/$', PlanItemAPIView.as_view(),name='plansitems')
]

