from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import generics ,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from Aggregator.api.rod import IsPostOwnerorReadonly,IsAuthorOrReadOnly
from Aggregator.api.serializers import Team_S,Testmonials_S,Course_S,Sites_S
from django_filters.rest_framework import DjangoFilterBackend
from Aggregator.models import Course,Sites,Testmonials,Team

class Testmonials_API(generics.ListCreateAPIView):
    queryset = Testmonials.objects.all()
    serializer_class = Testmonials_S
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    ordering_fields=["Date"]
    ordering=["Date"]
    def get_queryset(self):
        user = self.request.user
        return Testmonials.objects.order_by("-Date")

class Teams_API(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = Team_S


class Course_List(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = Course_S
    
    
class Course_List_Edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = Course_S
    lookup_field='pk'
# class StatusAPIView(APIView):
#         """Allow users to add/remove a like to/from an answer instance."""
#         serializer_class = Week_Status
#
#
#         def delete(self, request, id):
#             """Remove request.user from the voters queryset of an answer instance."""
#             answer = get_object_or_404(Week, id=id)
#             user = request.user
#
#             answer.view_status.remove(user)
#             answer.save()
#
#             serializer_context = {"request": request}
#             serializer = self.serializer_class(answer, context=serializer_context)
#
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         def post(self, request, id):
#             """Add request.user to the voters queryset of an answer instance."""
#             answer = get_object_or_404(Week, id=id)
#             user = request.user
#
#             answer.view_status.add(user)
#             answer.save()
#
#             serializer_context = {"request": request}
#             serializer = self.serializer_class(answer, context=serializer_context)
#
#             return Response(serializer.data, status=status.HTTP_200_OK)


