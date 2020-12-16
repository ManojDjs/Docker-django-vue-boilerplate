from django.urls import path
from Demographics.api.views import QuestionsAPI,AnswersAPI,TotalAnswersAPI,QuestionEditAPI,ListISQ_Questions,AnswersEditAPI
urlpatterns=[
    path('DQ_Q/',ListISQ_Questions.as_view(),name='user_questions'),
    path('DQ/',QuestionsAPI.as_view(),name='quesions'),
    path('DQ_Edit/<int:pk>',QuestionEditAPI.as_view(),name='Q_update'),
    path('DQ_A/',AnswersAPI.as_view(),name='answers'),
    path('DQ_A_EDIT/<int:pk>',AnswersEditAPI.as_view(),name='answers_edit'),
    path('DQ_Total/',TotalAnswersAPI.as_view(),name='total_answers'),

]

