from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class VaralOSDBAuthBackend(BaseBackend):
    """
    To authenticate users using also varal os db
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.using('vendor_os_db').get(username=username)
            return user if user.check_password(password) else None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.using('vendor_os_db').get(pk=user_id)
        except User.DoesNotExist:
            return None