from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_admin_user_on_both_databases(sender, instance, created, using):
    """
    WE use this method to save created users (staff users) in the admin panel
    in both databases.
    """
    if created:
        if instance.is_staff:
            print(using)
    return

post_save.connect(create_admin_user_on_both_databases(), sender=User)