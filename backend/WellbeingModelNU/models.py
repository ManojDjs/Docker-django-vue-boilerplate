from django.db import models

from users.models import User
# Create your models here.
class WBMNU_Questions(models.Model):
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
class WBMNU(models.Model):
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='WBMNU',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class WBMNU_answers(models.Model):
    main_question_set=models.ForeignKey(WBMNU,on_delete=models.CASCADE,related_name='WBMNU',default=1)
    question_name=models.ForeignKey(WBMNU_Questions,on_delete=models.CASCADE,related_name='WBMNU_name_for_answer')
    answer=models.TextField()
    answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_WBMNU')
    def __str__(self):
        return self.question_name.question
