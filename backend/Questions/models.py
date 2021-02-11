from django.db import models
from users.models import User
from Courses.models import Course
class Topic(models.Model):
    Topic_name=models.CharField(max_length=500)
    def __str__(self):
        return self.Topic_name
class Labels(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="Topic_Label")
    label_name=models.TextField(null=True,blank=True)
    label_at=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.topic_name+self.label_name

class Questions(models.Model):
    question_course=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="Topic_qsn")
    question_no=models.IntegerField()
    question=models.CharField(max_length=5000)
    question_types = [
        ('Options', 'Options'),
        ('YESNO', 'YES/NO'),
        ('Slider', 'Slider'),
        ('Text', 'Text'),
        ('Number', 'Number'),
    ]
    question_type = models.CharField(
        max_length=10,
        choices=question_types,
        default='Text',
    )
    quetions_free_text=models.TextField(null=True,blank=True)
    class Meta:
        ordering=['question_no']
    def __str__(self):
        return self.question
class Intial_BaseLine_Answer(models.Model):
    Initial_question_name = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='Initial_question',default=1)
    Initial_answer = models.TextField(null=True,blank=True,default=1)
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_initial',to_field="username")
    def __str__(self):
        return self.Answered_by.username

# class Initial_Answers(models.Model):
#     Initial_main_question_set=models.ForeignKey(Initial_Answer,on_delete=models.CASCADE,related_name='Initial_answers',default=1)
#     Initial_question_name=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='Initial_question')
#     Initial_answer=models.PositiveIntegerField()
#     Initial_answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='initial_answer')
#     class Meta:
#         unique_together=['Initial_question_name','Initial_answer_by']
#     def __str__(self):
#         return self.Initial_question_name.question
class Final_Answer(models.Model):
    Course_Final=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="Final_course",unique=True)
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_final',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class Final_Answers(models.Model):
    Final_main_question_set=models.ForeignKey(Final_Answer,on_delete=models.CASCADE,related_name='Final_answers',default=1)
    Final_question_name=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='Final_question')
    Final_answer=models.PositiveIntegerField()
    Final_answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Final_answer')
    class Meta:
        unique_together=['Final_question_name','Final_answer_by']
    def __str__(self):
        return self.Final_main_question_set.question


