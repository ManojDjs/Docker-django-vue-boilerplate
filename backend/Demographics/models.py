from django.db import models
from django.db import models
from users.models import User
# Create your models here.
class Demographic_Questions(models.Model):
    question_no=models.PositiveIntegerField()
    question=models.CharField(max_length=5000)
    question_types = [
        ('Optional', 'Optional'),
        ('Mandatory', 'Mandatory'),

    ]
    question_type = models.CharField(
        max_length=10,
        choices=question_types,
        default='Mandatory',
    )
    class Meta:
        ordering=['question_no']
    def __str__(self):
        return self.question
class Demographic(models.Model):
    Answered_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Demographic',to_field="username",unique=True)
    def __str__(self):
        return self.Answered_by.username

class Demographic_answers(models.Model):
    main_question_set=models.ForeignKey(Demographic,on_delete=models.CASCADE,related_name='Demo',default=1)
    question_name=models.ForeignKey(Demographic_Questions,on_delete=models.CASCADE,related_name='demo_question_nme_for_answer')
    answer=models.TextField()
    answer_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_Demographics')
    def __str__(self):
        return self.question_name.question
