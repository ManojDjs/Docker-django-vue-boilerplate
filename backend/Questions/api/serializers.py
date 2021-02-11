from rest_framework import serializers
from Questions.models import Topic,Labels,Questions,Intial_BaseLine_Answer
class Questions_S(serializers.ModelSerializer):
    class Meta:
        model=Questions
        fields="__all__"
class Topic_S(serializers.ModelSerializer):
    Topic_qsn=Questions_S(many=True,read_only=True)
    class Meta:
        model=Topic
        fields=["id","Topic_name","Topic_qsn"]
class Answers_checking_S(serializers.ModelSerializer):
    Initial_question=Questions_S(many=True,read_only=True)
    class Meta:
        model=Intial_BaseLine_Answer
        fields=["id","Initial_question_name","Initial_answer","Answered_by","Initial_question"]
