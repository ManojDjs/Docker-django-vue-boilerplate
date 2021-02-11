from django.urls import path
from Questions.api.views import Topic_API,Check_Answers
urlpatterns=[
    # path('Courses/',LIST_COURSES.as_view(),name='Courses_LIST'),
    # path('Courses/<str:slug>',Course_API.as_view(),name='Courses'),
    # path('Courses/<str:slug>', Weeks_API.as_view(), name='Week_LIST'),
    # path(r'Courses/Week/<int:id>', StatusAPIView.as_view(), name='view'),
path('Topic_API/', Topic_API.as_view(), name='Topic_API'),
path('Check_Answers/', Check_Answers.as_view(), name='Check_Answers'),


]

