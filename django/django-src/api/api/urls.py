from .views import BlogPostRudView, BlogImageListView, UserLoginAPIView, UserCreateAPIView
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
    url(r'^img/(?P<pk>\d+)/$', BlogImageListView.as_view(), name='post-img'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^signup/$', UserCreateAPIView.as_view(), name='signup'),
    url(r'^auth/token', obtain_jwt_token),
]