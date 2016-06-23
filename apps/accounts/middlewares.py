from django.conf import settings
from django.contrib.auth.models import AnonymousUser

import redis


class SessionUserMapMiddleware(object):
	"""
	Maps a logged-in user's id with the sessionid on redis
	"""

	def process_request(self, request, *args, **kwargs):

		sessionid = request.COOKIES.get(settings.SESSION_COOKIE_NAME)

		if (sessionid is not None) and (not isinstance(request.user, AnonymousUser)):
			redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
			redis_client.set(request.user.id, sessionid)