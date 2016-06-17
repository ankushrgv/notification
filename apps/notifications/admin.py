
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# Register your models here.

class MyAdmin(UserAdmin):
	fieldsets = (
		(
			None,{
				'fields':(
					'username',
					'password',
					'first_name',
					'last_name',
					'email',
					'is_active',
					'is_staff',
				),
			}
		),
	)
	list_display = ['username', 'first_name', 'last_name', 'is_active', 'is_staff' ]


admin.site.register(MyUser, MyAdmin)