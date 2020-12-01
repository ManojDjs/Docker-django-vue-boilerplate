from django.db import models
from users.models import User
class ISQ_Questions(models.Model):
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
class Initial_ISQ(models.Model):
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class ISQAnswer(models.Model):
    main_question_set=models.ForeignKey(Initial_ISQ,on_delete=models.CASCADE,related_name='ISQ',default=1)
    question_name=models.ForeignKey(ISQ_Questions,on_delete=models.CASCADE,related_name='question_nme_for_answer')
    answer=models.PositiveIntegerField()
    answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='answer_user')
    def __str__(self):
        return self.question_name.question

######################
######################
######################
#demo graphics
class Demographic_Questions(models.Model):
    demo_question_no=models.PositiveIntegerField()
    demo_question=models.CharField(max_length=5000)
    question_types = [
        ('Optional', 'Optional'),
        ('Mandatory', 'Mandatory'),

    ]
    demo_field_type = models.CharField(
        max_length=10,
        choices=question_types,
        default='Mandatory',
    )
    class Meta:
        ordering=['demo_question_no']
    def __str__(self):
        return self.question
class Demographic(models.Model):
    demo_Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Demographic',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class Demographic_answers(models.Model):
    demo_main_question_set=models.ForeignKey(Demographic,on_delete=models.CASCADE,related_name='ISQ',default=1)
    demo_question_name=models.ForeignKey(Demographic_Questions,on_delete=models.CASCADE,related_name='demo_question_nme_for_answer')
    demo_answer=models.PositiveIntegerField()
    demo_answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_Demographics')
    def __str__(self):
        return self.question_name.question
