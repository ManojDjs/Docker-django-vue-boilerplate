from django.db import models

# Create your models here

from users.models import User
# Create your models here.
class FWBMNU_Questions(models.Model):
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
class FWBMNU(models.Model):
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='FWBMNU',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class FWBMNU_answers(models.Model):
    main_question_set=models.ForeignKey(FWBMNU,on_delete=models.CASCADE,related_name='FWBMNU',default=1)
    question_name=models.ForeignKey(FWBMNU_Questions,on_delete=models.CASCADE,related_name='FWBMNU_name_for_answer')
    answer=models.TextField()
    answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_FWBMNU')
    def __str__(self):
        return self.question_name.question
