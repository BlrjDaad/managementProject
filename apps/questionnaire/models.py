from django.db import models
from datetime import datetime

from .constants import *
from ..accounts.models import Employee
from ..invitations.models import InvitationInfo


class Questionnaire(models.Model):
    date = models.DateTimeField(null=True, default=datetime.utcnow)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    invitation = models.ForeignKey(InvitationInfo, on_delete=models.SET_NULL, null=True)
    is_finished = models.BooleanField(default=False)
    

class RpsQuestionnaire(models.Model):
    date = models.DateTimeField(null=True, default=datetime.utcnow)

    is_finished = models.BooleanField(default=False)
    questionnaire_type = models.CharField(
        verbose_name='Type',
        choices=QuestionnaireType,
        max_length=50,
        default=QuestionnaireType[0][0]
    )
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)


class QuestionCategory(models.Model):
    category = models.CharField(max_length=200)
    score = models.IntegerField(null=True)


class QuestionCategoryQuestionnaire(QuestionCategory):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)


class RpsQuestionCategory(QuestionCategory):
    questionnaire = models.ForeignKey(RpsQuestionnaire, on_delete=models.CASCADE)


class Question(models.Model):
    question = models.TextField(null=True)
    answer = models.TextField(null=True)
    area = models.TextField(null=True)
    score = models.IntegerField(null=True)


class QuestionHealth(Question):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)


class RpsQuestion(Question):
    category = models.ForeignKey(RpsQuestionCategory, on_delete=models.CASCADE)
