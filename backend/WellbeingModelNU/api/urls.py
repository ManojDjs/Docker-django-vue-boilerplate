from django.urls import path
from WellbeingModelNU.api.views import QuestionsAPI,AnswersAPI,TotalAnswersAPI,QuestionEditAPI,ListISQ_Questions,AnswersEditAPI
urlpatterns=[
    path('WBMNU',ListISQ_Questions.as_view(),name='user_questions'),
    path('WBMNU/',QuestionsAPI.as_view(),name='quesions'),
    path('WBMNU_Edit/<int:pk>',QuestionEditAPI.as_view(),name='Q_update'),
    path('WBMNU_A/',AnswersAPI.as_view(),name='answers'),
    path('WBMNU_A_EDIT/<int:pk>',AnswersEditAPI.as_view(),name='answers_edit'),
    path('WBMNU_Total/',TotalAnswersAPI.as_view(),name='total_answers'),

]

