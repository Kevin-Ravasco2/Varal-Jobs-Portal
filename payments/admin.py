from django.contrib import admin

from payments.models import Payment, MTOPaymentStatus

admin.site.register(MTOPaymentStatus)
admin.site.register(Payment)
