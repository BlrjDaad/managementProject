from django.db import models
from datetime import datetime
from ..accounts.models import BaseUser
import uuid


class BaseInvitation(models.Model):
    subject = models.CharField(max_length=500, null=True)
    token = models.TextField(default=uuid.uuid4())
    send_at = models.DateTimeField(null=True, default=datetime.utcnow)
    is_expired = models.BooleanField(default=False)


class InvitationInfo(models.Model):

    email = models.EmailField(max_length=128)
    full_name = models.CharField(max_length=200, null=True)
    invitation = models.ForeignKey(BaseInvitation, on_delete=models.CASCADE)



