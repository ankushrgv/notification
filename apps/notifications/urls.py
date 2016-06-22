from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.notifications import views

urlpatterns = [
    url(r'^$', login_required(views.Index.as_view()), name='index'),
    url(r'^notification_form_submit/$', views.notification_form_submit, name="notification_form_submit"),
    # url(r'^box_status_form_submit/$', views.box_status_form_submit, name="box_status_form_submit"),
]