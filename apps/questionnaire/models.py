from django.db import models
from datetime import datetime

from .constants import *
from ..accounts.models import Employee
from ..invitations.models import BaseInvitation


class Questionnaire(models.Model):
    date = models.DateTimeField(null=True, default=datetime.utcnow)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name="questionnaires")
    invitation = models.ForeignKey(BaseInvitation, on_delete=models.SET_NULL, null=True, related_name="questionnaires")
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
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="RpsQuestionnaires")


class QuestionCategory(models.Model):
    category = models.CharField(max_length=200)
    score = models.IntegerField(null=True)


class QuestionCategoryQuestionnaire(QuestionCategory):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="categories")


class RpsQuestionCategory(QuestionCategory):
    questionnaire = models.ForeignKey(RpsQuestionnaire, on_delete=models.CASCADE, related_name="RpsCategories")


class Question(models.Model):
    question = models.TextField(null=True)
    answer = models.TextField(null=True)
    area = models.TextField(null=True)
    score = models.IntegerField(null=True)


class QuestionHealth(Question):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, related_name="questions")


class RpsQuestion(Question):
    category = models.ForeignKey(RpsQuestionCategory, on_delete=models.CASCADE, related_name="RpsQuestions")
