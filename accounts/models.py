from django.db import models
from users.models import User


class MTO(User):
    paypal_id = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
