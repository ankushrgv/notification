"""
musicgreed URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^', include('apps.notifications.urls', namespace='notify')),
    url(r'^admin/', admin.site.urls),
]
