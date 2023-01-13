from django.db import models

# Create your models here.

from django.db import models
from users.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string

# Create your models here.
class Course(models.Model):
    Name=models.CharField(max_length=300)
    Category=models.CharField(max_length=15,default='Computers')
    Description=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
    likes = models.ManyToManyField(User, related_name='likes_post')
    image = models.ImageField(upload_to='profile_pics', default="Dairy.png",null=True,blank=True)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs, ):  # new
        if not self.slug:
            random_s = generate_random_string()
            self.slug = slugify(self.Name) + '-' + random_s
        return super().save(*args, **kwargs)

class Sites(models.Model):
    Course_Name=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='User_Course')
    Site=models.CharField(max_length=15)
    Price=models.IntegerField(default=0)
    Site_URL=models.URLField(max_length=70)
    Date=models.DateTimeField(auto_now_add=True)
    Features=models.TextField()

    def __str__(self) -> str:
        return str(self.Course_Name.Name+"----"+self.Site)


class Team(models.Model):
    Name=models.CharField(max_length=10)
    Designation=models.CharField(max_length=10)
    Git=models.URLField(max_length=50)
    Facebook=models.URLField(max_length=50)
    Email=models.URLField(max_length=50)
    phone_Number=models.CharField(max_length=10)
    Description=models.TextField()

    def __str__(self) -> str:
        return self.Name

class Testmonials(models.Model):
    Heading=models.CharField(max_length=300)
    Description=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
    likes = models.ManyToManyField(User, related_name='likes_test')
    image = models.ImageField(upload_to='profile_pics', default="Course.png",null=True,blank=True)
    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs, ):  # new
        if not self.slug:
            random_s = generate_random_string()
            self.slug = slugify(self.Name) + '-' + random_s
        return super().save(*args, **kwargs)


