from .views import *
from .serializers import *

from django.conf.urls import url
# from django.urls import path
# from . import views

app_name='_User'

urlpatterns = [

    # 유저 api
    url(r'^users/$', UserCreateView.as_view(), name='users'),
    url(r'^users/(?P<id>\d+)/$', UserDetailView.as_view(), name='user'),

    # 카테고리 api
    url(r'^cates/(?P<id>\d+)/$', CateDetailView.as_view(), name='cate'),

    # 리뷰 등록 api
    url(r'^reviews/$', ReviewCreateView.as_view(), name='reviews'),

    # 유저-리뷰조회 api
    url(r'^users/(?P<user_id>\d+)/reviews/$', UserReviewListView.as_view(), name='user_reviews'),
    url(r'^users/(?P<user_id>\d+)/reviews/(?P<item_id>\d+)/$', UserReviewDetailView.as_view(), name='user_review'),

    # 아이템-리뷰조회 api
    url(r'^items/(?P<item_id>\d+)/reviews/$', ItemReviewListView.as_view(), name='user_reviews'),
    url(r'^items/(?P<item_id>\d+)/reviews/(?P<user_id>\d+)/$', ItemReviewDetailView.as_view(), name='user_review'),

    # 픽 등록 api
    url(r'^picks/$', PickCreateView.as_view(), name='picks'),

    # 유저-픽조회 api
    url(r'^users/(?P<user_id>\d+)/picks/$', UserPickListView.as_view(), name='user_picks'),
    url(r'^users/(?P<user_id>\d+)/picks/(?P<item_id>\d+)/$', UserPickDetailView.as_view(), name='user_pick'),

    # route 동기화
    url(r'^sync/$', SyncView.as_view(), name='sync'),

]