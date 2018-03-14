from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^items/$', ItemListView.as_view(), name='items'),
    url(r'^items/(?P<id>\d+)/$', ItemDetailView.as_view(), name='items-detail'),
    url(r'^routes/$', DistanceListView.as_view(), name='routes'),
]