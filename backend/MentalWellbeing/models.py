
# Create your models here.
from django.db import models
from users.models import User
# Create your models here.
class MWB_Questions(models.Model):
    question_no=models.PositiveIntegerField()
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
class MWB(models.Model):
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='MWB',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class MWB_answers(models.Model):
    main_question_set=models.ForeignKey(MWB,on_delete=models.CASCADE,related_name='MWB',default=1)
    question_name=models.ForeignKey(MWB_Questions,on_delete=models.CASCADE,related_name='MWB_name_for_answer')
    answer=models.TextField()
    answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_MWB')
    def __str__(self):
        return self.question_name.question
