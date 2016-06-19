
from django.views.generic.base import TemplateView

from apps.notifications import models

class Index(TemplateView):

	template_name = 'notifications/index.html'

	def get_context_data(self, **kwargs):

		user_id_value = self.request.user.id
		print "user_id_value = ", user_id_value
		context = super(Index, self).get_context_data(**kwargs)

		user_obj = models.MyUser.objects.get(id = user_id_value)
		notification_count = user_obj.new_notification_count


		notification_list = models.Notification.objects.order_by('-time_of_creation').filter(notified_user_id=user_id_value)
		print "notification_list = ", notification_list

		context['user_obj'] = user_obj
		context['notification_count'] = notification_count
		context['notifications'] = notification_list

		for item in notification_list:
			item.status = True
			item.save()

		user_obj.new_notification_count = 0
		user_obj.save()

		return context