from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    is_mto = models.BooleanField(default=True) # by default the user is an MTO.
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            super(User, self).save(using='vendor_os_db')
        except:
            super(User, self).save(using='varal_job_posting_db')
