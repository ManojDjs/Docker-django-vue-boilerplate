from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from Demographics.models import Demographic_Questions,Demographic_answers,Demographic
from Demographics.api.serializers import Question_S,Answer_S,TotalAnswers_A
from rest_framework import generics
class ListISQ_Questions(APIView):
    def get(self, request, format=None):
        a=Demographic_Questions.objects.all()
        s=Question_S(a,many=True)
        return Response(s.data)
class QuestionsAPI(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset=Demographic_Questions.objects.all()
    serializer_class=Question_S

class QuestionEditAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdminUser]
    queryset = Demographic_Questions.objects.all()
    serializer_class = Question_S
    lookup_field='pk'

class AnswersAPI(generics.ListCreateAPIView):
    queryset=Demographic_answers.objects.all()
    serializer_class=Answer_S
class AnswersEditAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Demographic_answers.objects.all()
    serializer_class = Answer_S
    lookup_field='pk'

class TotalAnswersAPI(generics.ListCreateAPIView):
    queryset=Demographic.objects.all()
    serializer_class=TotalAnswers_A

    def get_queryset(self):
        user = self.request.user
        return Demographic.objects.filter(Answered_by=user)

