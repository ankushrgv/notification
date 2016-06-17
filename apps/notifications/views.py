
from django.views.generic.base import TemplateView

from apps.notifications import models

class Index(TemplateView):

	template_name = 'notifications/index.html'

	def get_context_data(self, **kwargs):

		user_id = self.request.user.id
		print "user_id = ", user_id

		context = super(Index, self).get_context_data(**kwargs)
		
		user_obj = models.MyUser.objects.get(id = user_id)
		print "user_obj = ", user_obj
		context['user_obj'] = user_obj

		return context