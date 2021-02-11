from django.urls import path
from Courses.api.views import Dairy_API,Dairy_API_Update,Dairy_List_API#Course_API,StatusAPIView,Dairy_List_API,LIST_COURSES,Weeks_API,
urlpatterns=[
    # path('Courses/',LIST_COURSES.as_view(),name='Courses_LIST'),
    # path('Courses/<str:slug>',Course_API.as_view(),name='Courses'),
    # path('Courses/<str:slug>', Weeks_API.as_view(), name='Week_LIST'),
    # path(r'Courses/Week/<int:id>', StatusAPIView.as_view(), name='view'),
path('MyDairy/', Dairy_List_API.as_view(), name='Dairy_Label'),
    path('Dairy/', Dairy_API.as_view(), name='Dairy_LIST'),
    path('Dairy_update/<int:id>', Dairy_API_Update.as_view(), name='Dairy_LIST')

]

