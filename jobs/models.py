from django.db import models

from accounts.models import User


class MTOJobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Microtask(models.Model):
    name = models.CharField(max_length=300)
    cat_id = models.ForeignKey(MTOJobCategory, on_delete=models.PROTECT)
    target_date = models.DateField()
    description = models.TextField(max_length=1000)
    upload_job_sample = models.FileField(max_length=500)
    upload_job_instructions = models.FileField(max_length=500)
    job_quantity = models.IntegerField()
    number_of_people_required = models.IntegerField()
    skills = models.CharField(max_length=500)
    job_cost = models.IntegerField(help_text="job cost in AED")

    def __str__(self):
        return self.name


class EvaluationStatus(models.Model):
    description = models.ForeignKey(Microtask, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class MTOJob(models.Model):
    job_id = models.ForeignKey(Microtask, on_delete=models.PROTECT)
    assigned_to = models.IntegerField(help_text='related to MTO')
    due_date = models.DateField()
    assigned_date = models.DateField()
    fees = models.FloatField()
    rating_evaluation = models.IntegerField()
    payment_status = models.IntegerField() # select a relationship
    completed_date = models.DateField()
    output_path = models.FileField()
    evaluation_status = models.ForeignKey(EvaluationStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_id + ' ' + self.assigned_to.full_name


class MTORoles(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class MTOAdminUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_user')
    # full_name = models.CharField(max_length=100)
    varal_role_id = models.ForeignKey(MTORoles, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name_plural = 'MTO Admin Users'


