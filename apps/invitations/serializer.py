from rest_framework import serializers
from .models import *


class InvitationInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvitationInfo
        fields = ["pk",
                  "email",
                  "full_name"]


# Serializers define the API representation.
class EmployeeInvitationSerializer(serializers.HyperlinkedModelSerializer):
    invitations_infos = InvitationInfoSerializer(many=True, required=False)

    class Meta:
        model = EmployeeInvitation
        fields = ["pk",
                  "subject",
                  "token",
                  "send_at",
                  "is_expired",
                  "invitations_infos"
                  ]





