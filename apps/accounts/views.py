from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.edit import FormView

from .forms import LoginForm


class LoginView(FormView):

    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('notifications:index')

    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated():
            return redirect(self.success_url)

        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form, *args, **kwargs):
        user = form.get_user()
        login(self.request, user)

        return super(LoginView, self).form_valid(form, *args, **kwargs)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('notifications:index'))
