"""Tour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# for image schema by jy
from django.conf import settings
from django.conf.urls.static import static

# original imports
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/', include('_Plan.api.urls', namespace='Plan_api')),
    url(r'^api/', include('_User.api.urls', namespace='User_api')),
    url(r'^api/', include('_Item.api.urls', namespace='Item_api')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)