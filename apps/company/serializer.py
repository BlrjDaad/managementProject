from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import serializers


# Serializers define the API representation.
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ['name',
                  'description',
                  'logo',
                  'logo_name']


# Serializers define the API representation.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['name',
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
                  'departments']





