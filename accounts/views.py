from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View

from accounts.forms import SignUpForm
from accounts.models import MTO


class SignUpView(View):
    template_name = 'accounts/register.html'

    def get(self, *args, **kwargs):
        form = SignUpForm
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        # check if there's need to handle race condition when creating users
        form = SignUpForm(self.request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('account_login'))


@login_required
def dummy_home_view(request):
    mtos = MTO.objects.using('vendor_os_db').all()
    context = {'mtos': mtos}
    return render(request, 'index.html', context)

