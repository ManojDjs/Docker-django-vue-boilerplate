from rest_framework import serializers
from users.models import User,Registered
class UserDetails(serializers.ModelSerializer):
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
        "last_name"]
class UserEdit(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username",'first_name',"last_name"]
class Registered_S(serializers.ModelSerializer):
    class Meta:
        model=Registered
        fields="__all__"