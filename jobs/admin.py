from django.contrib import admin

from jobs.models import MTOAdminUser, MTOJobCategory, MTORoles, Microtask, MTOJob, EvaluationStatus

admin.site.register(EvaluationStatus)
admin.site.register(MTOAdminUser)
admin.site.register(MTOJob)
admin.site.register(MTOJobCategory)
admin.site.register(MTORoles)
admin.site.register(Microtask)


