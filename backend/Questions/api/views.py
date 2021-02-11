from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import generics ,status
from rest_framework.generics import get_object_or_404
from Courses.api.rod import IsPostOwnerorReadonly
from django_filters.rest_framework import DjangoFilterBackend
from Questions.models import Topic,Labels,Questions,Intial_BaseLine_Answer
from Questions.api.serializers import Topic_S,Questions_S,Answers_checking_S

class Topic_API(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = Topic_S
    permission_classes = [IsPostOwnerorReadonly, IsAuthenticated]
class Check_Answers(generics.ListCreateAPIView):
    queryset = Intial_BaseLine_Answer.objects.all()
    serializer_class = Answers_checking_S
    permission_classes = [IsPostOwnerorReadonly, IsAuthenticated]



# class Dairy_API_Update(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Dairy.objects.all()
#     serializer_class = Dairy_S
#     lookup_field = "id"


