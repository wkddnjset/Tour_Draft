from .views import BlogPostRudView
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
]
