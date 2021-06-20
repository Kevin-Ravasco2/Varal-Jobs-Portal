from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from users.forms import MTOAdminAuthenticationForm


class MTOAdminLoginView(LoginView):
    template_name = 'admin_login.html'
    authentication_form = MTOAdminAuthenticationForm

    def form_valid(self, form):
        """Security check complete. Log the mto admin  in and redirect."""
        login(self.request, form.get_user())
        return HttpResponseRedirect('/some-success-url/')
