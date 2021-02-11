from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image

class User(AbstractUser):
    username = models.CharField(
        _('username'), unique=True, max_length=50,
        validators=[MinLengthValidator(2),])
    password = models.CharField(_('password'), max_length=128)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default="default.jpg")

    # default = 'path/to/my/default/image.jpg'
    def __str__(self):
        return f'{self.user.username} Profile'

    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    post_save.connect(create_profile,sender=User)
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
class Registered(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Initiated',to_field="username")
    def __str__(self):
        return f'{self.user.username} Registered with the system'

