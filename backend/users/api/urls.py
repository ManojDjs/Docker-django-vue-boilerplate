from django.urls import path
from users.api.views import UserDetailsAPI,UserEditAPI,Register_view,Register_status,Profile_View
urlpatterns=[
    path('userdetails',UserDetailsAPI.as_view(),name='user_details'),
    path('useredit/<int:pk>', UserEditAPI.as_view(), name='user_edit'),
path('Register_view/', Register_view.as_view(), name='Register_view'),
path('Register_status/', Register_status.as_view(), name='Register_status'),
path('Profile/', Profile_View.as_view(), name='Profile_View'),


]

