from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    """
    Renders and validates the login form.
    """

    user = None

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            self.user = user
            return cleaned_data

        raise forms.ValidationError('Username and password do not match.')

    def get_user(self):
        if hasattr(self, 'user'):
            return getattr(self, 'user')
        return None
