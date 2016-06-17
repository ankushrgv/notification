from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.notifications import views

urlpatterns = [
    url(r'^$', login_required(views.Index.as_view()), name='index'),
]