from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.conf import settings  # noqa

from datetime import timedelta
import random

app = Celery('config')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

t = random.randint(45, 85)
print "time = ", t

## celery app configuration
app.conf.CELERYBEAT_SCHEDULE = {
    # Executes at every 't' interval, where t is random
    'create-notifications': {
        'task': 'apps.notifications.tasks.CreateNotifications',
        'schedule': timedelta(seconds=t),
    },
}
app.conf.CELERY_TIMEZONE = 'Asia/Kolkata'