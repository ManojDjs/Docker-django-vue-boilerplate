from django.urls import path
from FMentalWellbeing.api.views import QuestionsAPI,AnswersAPI,TotalAnswersAPI,QuestionEditAPI,ListISQ_Questions,AnswersEditAPI
urlpatterns=[
    path('MWB',ListISQ_Questions.as_view(),name='user_questions'),
    path('MWB/',QuestionsAPI.as_view(),name='quesions'),
    path('MWB_Edit/<int:pk>',QuestionEditAPI.as_view(),name='Q_update'),
    path('MWB_A/',AnswersAPI.as_view(),name='answers'),
    path('MWB_A_EDIT/<int:pk>',AnswersEditAPI.as_view(),name='answers_edit'),
    path('MWB_Total/',TotalAnswersAPI.as_view(),name='total_answers'),

]

