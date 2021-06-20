from django import forms
from django.contrib.auth.forms import AuthenticationForm


class MTOAdminAuthenticationForm(AuthenticationForm):

    def clean(self):
        super().clean()
        if self.user_cache is not None and self.user_cache.is_mto:
            raise forms.ValidationError('Invalid username or password', code='invalid login')
