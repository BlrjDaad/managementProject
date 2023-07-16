from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import *
from ..accounts.serializer import EmployeeSerializer, ManagerSerializer
from ..invitations.serializer import EmployeeInvitationSerializer


# Serializers define the API representation.
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    employees = EmployeeSerializer(many=True, required=False)
    invitations = EmployeeInvitationSerializer(many=True, required=False)

    class Meta:
        model = Department
        fields = ['pk',
                  'name',
                  'description',
                  'logo',
                  'logo_name',
                  'employees',
                  'invitations']


# Serializers define the API representation.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    departments = DepartmentSerializer(many=True, required=False)
    managers = ManagerSerializer(many=True, required=False)

    class Meta:
        model = Company
        fields = ['pk',
                  'name',
                  'description',
                  'universal_name',
                  'company_type',
                  'status',
                  'employee_count_range',
                  'specialities',
                  'location',
                  'founded_year',
                  'all_over_threshold',
                  'invitation_paused',
                  'date_expiration',
                  'paid',
                  'sending_interval',
                  'departments',
                  'managers']





