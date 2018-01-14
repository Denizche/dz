"""Lab_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Lab5_App.views import *

urlpatterns = [
    url(r'^function_view/', function_view),
    url(r'^class_b_view/', ClassBased.as_view()),
    url(r'^allorders/(?P<id>\d+)', order_info, name='orderinfo_url'),
    url(r'^allorders/', AllOrders.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^order/', order_add, name='order_url'),
    url(r'^service/(?P<id>\d+)', service_info, name='service_url'),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^$', OrdersList.as_view(), name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
