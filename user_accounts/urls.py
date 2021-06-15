from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user_accounts.views import SignUpView, dummy_home_view

urlpatterns = [
    path('', dummy_home_view, name='home'),

    # authentication patterns
    path('register/', SignUpView.as_view(), name='account_signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
]