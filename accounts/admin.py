from django.contrib import admin
from .models import MTO

admin.site.register(MTO)


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    vendor_os_db = 'vendor_os_db'
    job_posting_db = 'varal_job_posting_db'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        # obj.save(using=self.vendor_os_db)
        # obj.save(using=self.job_posting_db)
        obj.save()
