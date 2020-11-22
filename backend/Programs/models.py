from django.db import models
from users.models import User
class ISQ_Questions(models.Model):
    question_no=models.IntegerField()
    question=models.CharField(max_length=5000)

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
