from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.db.models.signals import post_save

# Create your models here.

class MyUser(AbstractUser):
	notification_count = models.IntegerField(default=0)
