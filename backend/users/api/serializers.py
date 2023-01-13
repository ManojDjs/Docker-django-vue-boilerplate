from rest_framework import serializers
from users.models import User,Registered,Profile
from django.core import serializers as c
from rest_framework.renderers import JSONRenderer
import json
class Profile_SE(serializers.ModelSerializer):
    class Meta:
        Model=Profile
        fields=['image']
class UserDetails(serializers.ModelSerializer):
    # Profile_PIC=Profile_SE(many=True, read_only=True)
    class Meta:
        model=User
        fields=[
        "id",
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "username",
        "email",
        "first_name",
        "last_name",
        "Image"
        ]
class UserEdit(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username",'first_name',"last_name"]
class Registered_S(serializers.ModelSerializer):
    class Meta:
        model=Registered
        fields="__all__"

class Profile_S(serializers.ModelSerializer):
    Profile_PIC=UserDetails(many=True, read_only=True)
    class Meta:
        model=Profile
        fields=["id",
        "image",
        "Profile_PIC"]