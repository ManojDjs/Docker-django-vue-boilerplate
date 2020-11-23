from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from Programs.models import ISQ_Questions,ISQAnswer,Initial_ISQ
from Programs.api.serializers import Question_S,Answer_S,TotalAnswers_A
from rest_framework import generics
class ListISQ_Questions(APIView):
    def get(self, request, format=None):
        a=ISQ_Questions.objects.all()
        s=Question_S(a,many=True)
        return Response(s.data)
class QuestionsAPI(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset=ISQ_Questions.objects.all()
    serializer_class=Question_S
class QuestionEditAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdminUser]
    queryset = ISQ_Questions.objects.all()
    serializer_class = Question_S
    lookup_field='pk'

class AnswersAPI(generics.ListCreateAPIView):
    queryset=ISQAnswer.objects.all()
    serializer_class=Answer_S
class TotalAnswersAPI(generics.ListCreateAPIView):
    queryset=Initial_ISQ.objects.all()
    serializer_class=TotalAnswers_A

