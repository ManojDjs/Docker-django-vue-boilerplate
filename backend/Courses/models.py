from django.db import models
from users.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
# Create your models here.
class Course(models.Model):
    Name=models.CharField(max_length=300)
    Description=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
    likes = models.ManyToManyField(User, related_name='likes_courses')
    image = models.ImageField(upload_to='profile_pics', default="Dairy.png",null=True,blank=True)
    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs, ):  # new
        if not self.slug:
            random_s = generate_random_string()
            self.slug = slugify(self.Name) + '-' + random_s
        return super().save(*args, **kwargs)
class Enrolled(models.Model):
    Course_Enrolled = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='User_Course')
    Enrolled_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Enrolled', default=1)
    def __str__(self):
        return str(self.Course_Enrolled.Name)+"-week-"+str(self.Enrolled_User)


class Week(models.Model):
    Course_Week=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='Course_week')
    Week_number=models.IntegerField()
    Week_name=models.CharField(max_length=200)
    view_status = models.ManyToManyField(User, related_name='View_status')
    def __str__(self):
        return str(self.Course_Week.Name)+"-week-"+str(self.Week_number)

class Video(models.Model):
    Video_week=models.ForeignKey(Week,on_delete=models.CASCADE,related_name='Video_Week',default=1)
    Video_URL=models.URLField(max_length=3000)
    Video_Name=models.CharField(max_length=300)
    Video_Description=models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    Dairy_Description=models.TextField(default="please add your dairy after seeing video")
    def __str__(self):
        return str(self.Video_week)+"--->"+str(self.Video_week.Week_number)+str(self.Video_Name)
    def save(self, *args, **kwargs, ):  # new
        if not self.slug:
            random_s = generate_random_string()
            self.slug = slugify(self.Video_Name) + '-' + random_s
        return super().save(*args, **kwargs)
class DairyLabel(models.Model):
    DairyNumber=models.IntegerField(default=1)
    Text=models.TextField()
    def __str__(self):
        return self.Text
class Dairy(models.Model):
    Dairy_label=models.ForeignKey(DairyLabel,on_delete=models.CASCADE,related_name='Dairy_label',default=1)
    Date=models.DateTimeField(auto_now_add=True)
    Dairy_Text=models.TextField()
    Wrote_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Dairy',default=1)
    class Meta:
        unique_together=['Date','Wrote_by']
    def __str__(self):
        return str(self.Wrote_by.username)+"--->"+str(self.Date)


