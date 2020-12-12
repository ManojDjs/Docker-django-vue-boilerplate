from django.urls import path
from users.api.views import UserDetailsAPI,UserEditAPI
urlpatterns=[
    path('userdetails',UserDetailsAPI.as_view(),name='user_details'),
    path('useredit/<int:pk>', UserEditAPI.as_view(), name='user_edit'),

]

