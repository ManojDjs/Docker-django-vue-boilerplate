from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.api.serializers import UserDetails,UserEdit
from rest_framework import generics
class UserDetailsAPI(APIView):
    def get(self, request, format=None):
        a=User.objects.filter(username=request.user)
        s=UserDetails(a,many=True)
        return Response(s.data)
class UserEditAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserEdit
    lookup_field='pk'



