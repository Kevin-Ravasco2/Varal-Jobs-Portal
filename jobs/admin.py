from django.contrib import admin

from jobs.models import MTOAdminUsers, MTOJobCategory, MTORoles, Microtask, MTOJob, EvaluationStatus

admin.site.register(EvaluationStatus)
admin.site.register(MTOAdminUsers)
admin.site.register(MTOJob)
admin.site.register(MTOJobCategory)
admin.site.register(MTORoles)
admin.site.register(Microtask)


