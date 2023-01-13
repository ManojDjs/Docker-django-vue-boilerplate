from django.urls import path
from Aggregator.api.views import Teams_API,Testmonials_API,Course_List_Edit,Course_List
urlpatterns=[
    path('Testmonials/', Testmonials_API.as_view(), name='Testmonials'),
    path('Team/', Teams_API.as_view(), name='Team'),
    path('Course_List/', Course_List.as_view(), name='Course_List'),
    path('Course_List_Edit/', Course_List_Edit.as_view(), name='Course_List_Edit')

]

