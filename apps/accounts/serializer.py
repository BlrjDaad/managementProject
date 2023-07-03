from .models import *
from rest_framework import serializers


# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ['username', 'email', 'role', 'subrole', 'first_name', 'enabled', 'member_since', 'last_seen', 'deleted_at',
                  'first_connection', 'welcome_msg']



