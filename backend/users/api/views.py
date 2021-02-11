from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User,Registered
from users.api.serializers import UserDetails,UserEdit,Registered_S
from Courses.api.rod import IsPostOwnerorReadonly
from rest_framework.permissions import IsAdminUser,IsAuthenticated
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
class Register_view(generics.ListCreateAPIView):
    queryset = Registered.objects.all()
    serializer_class = Registered_S
    permission_classes = [IsPostOwnerorReadonly, IsAuthenticated]
class Register_status(APIView):
    def get(self, request, format=None):
        a=Registered.objects.filter(user=request.user)
        s=Registered_S(a,many=True)
        return Response(s.data)



