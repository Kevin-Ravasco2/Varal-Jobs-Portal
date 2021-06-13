
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    is_mto = models.BooleanField(default=False, help_text="Means user can login to dean's portal")
    is_archived = models.BooleanField(default=False, help_text="Means User account has been deactivated")
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True,
                                   help_text="means last time table instance was edited")
    created = models.DateTimeField(_('Created'), auto_now_add=True, null=True,
                                   help_text="time table instance was created")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.email}'

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def _allow_edit(obj=None):
        if not obj:
            return True
        return not (obj.is_superuser or obj.staff)

    def has_perm(self, request, obj=None):
        return True


class MTO(User):
    paypal_id = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

