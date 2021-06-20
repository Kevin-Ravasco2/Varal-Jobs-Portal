from django.contrib.auth.views import LoginView

from users.forms import MTOAdminAuthenticationForm


class MTOAdminLoginView(LoginView):
    template_name = 'admin_login.html'
    authentication_form = MTOAdminAuthenticationForm
    success_url = 'mto/' # please change this url to the admin dashboard url
