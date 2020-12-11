from django.db import models

# Create your models here.
from django.db import models
from users.models import User
class FISQ_Questions(models.Model):
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
    class Meta:
        ordering=['question_no']
    def __str__(self):
        return self.question
class Final_ISQ(models.Model):
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Fuser',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class FISQAnswer(models.Model):
    main_question_set=models.ForeignKey(Final_ISQ,on_delete=models.CASCADE,related_name='FISQ',default=1)
    question_name=models.ForeignKey(FISQ_Questions,on_delete=models.CASCADE,related_name='question_name_for_Fanswer')
    answer=models.PositiveIntegerField()
    answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='answer_Fuser')
    class Meta:
        unique_together=['question_name','answer_by']
    def __str__(self):
        return self.question_name.question

######################
######################
######################
#demo graphics
