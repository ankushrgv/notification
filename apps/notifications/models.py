from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.db.models.signals import post_save

# Create your models here.

class MyUser(AbstractUser):
	new_notification_count = models.IntegerField(default=0)

class Notification(models.Model):
	notified_user = models.ForeignKey(MyUser, related_name='notified_user')
	notifier = models.ForeignKey(MyUser, related_name='notifier')
	notification_type = models.CharField( max_length=15 ) ## comment, like or share
	notification_media = models.CharField( max_length=15 )  ## post, picture, video
	status = models.BooleanField(default=False)  ## read or unread
	time_of_creation = models.DateTimeField(auto_now=True, auto_now_add=False)