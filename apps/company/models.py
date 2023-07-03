from django.db import models

from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    universal_name = models.CharField(max_length=150, null=True)
    company_type = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    employee_count_range = models.CharField(max_length=100, null=True)
    specialities = models.CharField(max_length=150, null=True)
    location = models.TextField(null=True)
    founded_year = models.CharField(max_length=150, null=True)
    all_over_threshold = models.IntegerField(default=20)
    invitation_paused = models.BooleanField(default=True)
    date_expiration = models.DateTimeField(null=True, default=datetime.utcnow)
    paid = models.BooleanField(default=True)
    sending_interval = models.IntegerField(default=1)


def get_user_media_folder(instance, filename):
    return "company/%s/avatar_%s_%s" % (
        instance.pk,
        datetime.now(),
        filename)


class Department(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(default="")
    logo = models.ImageField(
        verbose_name='Avatar',
        upload_to=get_user_media_folder,
        null=True,
        blank=True,
    )
    logo_name = models.CharField(max_length=255, null=True)
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)
