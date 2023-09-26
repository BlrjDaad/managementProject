from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = QuestionHealth
        fields = ["pk",
                  "question",
                  "score"]


class RpsQuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RpsQuestion
        fields = ["pk",
                  "question",
                  "score"]


class QuestionCategorySerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = QuestionCategoryQuestionnaire
        fields = ["pk",
                  "category",
                  "score",
                  "questions"]


class RpsQuestionCategorySerializer(serializers.HyperlinkedModelSerializer):
    RpsQuestions = RpsQuestionSerializer(many=True, required=False)

    class Meta:
        model = RpsQuestionCategory
        fields = ["pk",
                  "category",
                  "score",
                  "RpsQuestions"
                  ]


class QuestionnaireRpsSerializer(serializers.HyperlinkedModelSerializer):
    categories = RpsQuestionCategorySerializer(many=True, required=False)

    class Meta:
        model = RpsQuestionnaire
        fields = ["pk",
                  "date",
                  "questionnaire_type",
                  "is_finished",
                  "RpsCategories"]


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    RpsQuestionnaires = QuestionnaireRpsSerializer(many=True, required=False)
    categories = QuestionCategorySerializer(many=True, required=False)

    class Meta:
        model = Questionnaire
        fields = ["pk",
                  "date",
                  "is_finished",
                  "RpsQuestionnaires",
                  "categories"]




