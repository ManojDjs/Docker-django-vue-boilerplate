
# Create your models here.
from django.db import models
from users.models import User
# Create your models here.
class FMWB_Questions(models.Model):
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
class FMWB(models.Model):
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FMWB',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class FMWB_answers(models.Model):
    main_question_set=models.ForeignKey(FMWB,on_delete=models.CASCADE,related_name='FMWB',default=1)
    question_name=models.ForeignKey(FMWB_Questions,on_delete=models.CASCADE,related_name='FMWB_name_for_answer')
    answer=models.TextField()
    answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_FMWB')
    def __str__(self):
        return self.question_name.question
