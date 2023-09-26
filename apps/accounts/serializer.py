from .models import *
from rest_framework import serializers
from ..questionnaire.serializer import QuestionnaireSerializer


# Serializers define the API representation.
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    questionnaires = QuestionnaireSerializer(many=True, required=False)

    class Meta:
        model = Employee
        fields = ['pk',
                  'username',
                  'email',
                  'role',
                  'subrole',
                  'first_name',
                  'enabled',
                  'member_since',
                  'last_seen',
                  'deleted_at',
                  'first_connection',
                  'welcome_msg',
                  'questionnaires']


class ManagerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Manager
        fields = ['pk',
                  'username',
                  'email',
                  'role',
                  'subrole',
                  'first_name',
                  'enabled',
                  'member_since',
                  'last_seen',
                  'deleted_at',
                  'first_connection']



