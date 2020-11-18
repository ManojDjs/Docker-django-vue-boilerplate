from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
# Create your models here.
class Programs(models.Model):
    program_name=models.CharField(max_length=256)
    program_startdate=models.DateTimeField(auto_now=True)
    program_description=models.TextField()
    # likes=models.ManyToManyField()

    def __str__(self):
        return self.program_name
class EnrolledPrograms(models.Model):
    enrolled_program=models.ForeignKey(Programs,related_name='program_enrolled',on_delete=models.CASCADE)
    student=models.ForeignKey(django.contrib.auth.get_user_model(),related_name='student_enrolled',on_delete=models.CASCADE)
    enrolled_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.enrolled_program