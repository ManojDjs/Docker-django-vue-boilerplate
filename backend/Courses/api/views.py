from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Courses.models import Course,Week,Video,Dairy,DairyLabel

from Courses.api.serializers import Course_S,Week_S,Dairy_S,Course_LIST_S,Week_Status,Dairy_label
from rest_framework import generics
from rest_framework import generics ,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from Courses.api.rod import IsPostOwnerorReadonly
from django_filters.rest_framework import DjangoFilterBackend

class Dairy_List_API(APIView):
    def get(self, request, format=None):
        a = DairyLabel.objects.all()
        s = Dairy_label(a, many=True)
        return Response(s.data)

class Dairy_API(generics.ListCreateAPIView):
    queryset = DairyLabel.objects.all()
    serializer_class = Dairy_S
    permission_classes = [IsPostOwnerorReadonly, IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    ordering_fields=["Date"]
    ordering=["Date"]
    def get_queryset(self):
        user = self.request.user
        return Dairy.objects.filter(Wrote_by=user).order_by("-Date")

class Dairy_API_Update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dairy.objects.all()
    serializer_class = Dairy_S
    lookup_field = "id"
    permission_classes = [IsPostOwnerorReadonly,IsAuthenticated]
class LIST_COURSES(APIView):
    def get(self, request, format=None):
        a=Course.objects.all()
        s=Course_LIST_S(a,many=True)
        return Response(s.data)
class Course_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = Course_S
    lookup_field = 'slug'

class Weeks_API(generics.ListCreateAPIView):
    queryset = Week.objects.all()
    serializer_class = Week_S
    lookup_field = 'slug'
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


