from django.db import models
from datetime import datetime
from ..accounts.models import BaseUser
from ..company.models import Department
import uuid


class InvitationInfo(models.Model):
    email = models.EmailField(max_length=128)
    full_name = models.CharField(max_length=200, null=True)


class BaseInvitation(models.Model):
    subject = models.CharField(max_length=500, null=True)
    token = models.TextField(default=uuid.uuid4())
    send_at = models.DateTimeField(null=True, default=datetime.utcnow)
    is_expired = models.BooleanField(default=False)
    invitations_infos = models.ForeignKey(InvitationInfo,
                                          related_name="invitations_info",
                                          on_delete=models.CASCADE)


class EmployeeInvitation(BaseInvitation):
    department = models.ForeignKey(Department, related_name='invitations', on_delete=models.CASCADE)
