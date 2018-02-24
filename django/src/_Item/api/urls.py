from .views import ItemListView
from django.conf.urls import url

urlpatterns = [
    url(r'^items/$', ItemListView.as_view(), name='items'),
]