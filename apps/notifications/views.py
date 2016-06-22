
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from apps.notifications import models

import datetime
import json
import redis

class Index(TemplateView):

	template_name = 'notifications/index.html'

	def get_context_data(self, **kwargs):

		user_id_value = self.request.user.id
		print "user_id_value = ", user_id_value
		context = super(Index, self).get_context_data(**kwargs)

		user_obj = models.MyUser.objects.get(id = user_id_value)
		notification_count = user_obj.new_notification_count


		notification_list = models.Notification.objects.order_by('-time_of_creation').filter(notified_user_id=user_id_value)

		# if user_obj.box_status == 1:
		# 	print " inside box open "
		# 	for item in notification_list:
		# 		if item.status == 0:
		# 			item.status = 1
		# 			item.save()

		# 	user_obj.box_status = 0
		# 	user_obj.new_notification_count = 0
		# 	user_obj.save()

		# 	notification_count = 0


		# print "notification_list = ", notification_list

		# i = 0
		# n = len(notification_list)

		# while i < n:
		# 	if i > (notification_count-1):
		# 		notification_list[i].status = 1
		# 		notification_list[i].save()
		# 	i += 1

		print "notification_count = ", notification_count

		context['user_obj'] = user_obj
		context['notification_count'] = notification_count
		context['notifications'] = notification_list

		# item_list = []
		# item_list = notification_list

		# for item in item_list:
		#   item.status = True
		#   item.save()

		# user_obj.new_notification_count = 0
		# user_obj.save()

		return context


@receiver(post_save, sender=models.Notification)
def on_notification_post_save(sender, created, **kwargs):
	print "post save signal triggered"
	if created:
		print "New notification created (post save)"
		redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
		notification = kwargs['instance']
		recipient = notification.notified_user
		print "Recipient: %s" % recipient.id

		# for session in recipient.session_set.all():
		datetime.timedelta(0,5,30)
		t = notification.time_of_creation
		t = t + datetime.timedelta(hours=5, minutes=30)
		t = str(t)
		t = t[:-13]

		notifier_name = notification.notifier.first_name + " " + notification.notifier.last_name
		print " notifier name = ", notifier_name

		redis_client.publish(
			'notifications.%s' % recipient.id,
			json.dumps(
				dict(
					timestamp=t,
					recipient=notification.notified_user.id,
					actor=notifier_name,
					verb=notification.notification_type,
					action_object=notification.notification_media,
					notification_id=notification.id 
				)
			)
		)


def notification_form_submit(request):
	
	if request.method == 'POST':

		content = request.POST
		print content

		myDict = dict(content.iterlists())

		user_id = myDict['user_id']
		# box_status = myDict['box_status']

		user_obj = models.MyUser.objects.get(id=int(user_id[0]))
		
		# if box_status[0] == 'open':
		# 	print "box is open1"
		# 	user_obj.box_status = 1
		# else:
		# 	print "box is close1"
		# 	user_obj.box_status = 0

		# user_obj.save()

		unread_list = []

		try:
			unread_list = myDict['notific_id']
			print "try"
		except:
			print "except"
			pass

		if unread_list:
			print "if"
			for item in unread_list:
				print "item = ", item
				obj = models.Notification.objects.get(id=int(item))
				obj.status = 1
				obj.save()

			user_obj.new_notification_count = 0
			user_obj.save()

		return HttpResponse(
			 json.dumps({'status': 'True'})
		)

	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"})
		)


# def box_status_form_submit(request):
	
# 	if request.method == 'POST':

# 		content = request.POST
# 		print content

# 		user_id = []

# 		user_id= content['user_id']
		
# 		user_obj = models.MyUser.objects.get(id=int(user_id[0]))
# 		user_obj.box_status = 0
# 		user_obj.save()

# 		print "box status = ", user_obj.box_status

# 		return HttpResponse(
# 			 json.dumps({'status': 'True'})
# 		)

# 	else:
# 		return HttpResponse(
# 			json.dumps({"nothing to see": "this isn't happening"})
# 		)