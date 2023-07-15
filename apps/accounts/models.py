from django.contrib.auth.models import AbstractBaseUser

from ..company.models import *
from .constants import *


class Role:
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 4


class Permissions(models.Model):
    code = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)


class BaseUser(AbstractBaseUser):
    username = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    role = models.IntegerField(default=3)
    subrole = models.IntegerField(default=2)

    first_name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )

    enabled = models.BooleanField(default=True)
    member_since = models.DateTimeField(null=True, default=datetime.utcnow)
    last_seen = models.DateTimeField(null=True, default=datetime.utcnow)
    deleted_at = models.DateTimeField(null=True)
    first_connection = models.BooleanField(default=True)
    welcome_msg = models.BooleanField(default=True)
    permissions = models.CharField(
        max_length=10000,
        default=""
    )

    def add_role(self, role):
        if not self.has_role(role):
            self.role += role

    def remove_role(self, role):
        if self.has_role(role):
            self.role -= role

    def reset_role(self):
        if self.role != 0:
            self.role = 0

    def has_role(self, role):
        return self.role & role == role


class Employee(BaseUser):
    info_deleted = models.BooleanField(default=False)
    accept_medical_sharing = models.BooleanField(default=False)
    assigned_to_company = models.BooleanField(default=False)
    update_email = models.BooleanField(default=False)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)


class MedicalRecord(models.Model):

    sexe = models.CharField(
        choices=GENDER,
        max_length=50,
        default=GENDER[0][0]
    )
    age = models.IntegerField()
    weight = models.IntegerField()
    tall = models.IntegerField()
    profession = models.CharField(max_length=200)
    home_work = models.CharField(
        choices=HOME_WORK,
        max_length=50,
        default=HOME_WORK[0][0]
    )
    sleep = models.FloatField()
    cigarettes = models.IntegerField(null=True, default=0)
    working_hours = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Manager(BaseUser):
    company = models.ForeignKey(Company, related_name='managers',
                                on_delete=models.SET_NULL, blank=True, null=True)
