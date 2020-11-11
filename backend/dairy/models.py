from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User , Group
# Create your models here.
class Program(models.Model):
    Status = [
        (0, 'enroll'),
        (1, 'start'),
        (2, 'middle'),
        (3, 'completed'),
        (4, 'Un-enroll'),
    ]
    program_name=models.CharField(max_length=200)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status=models.IntegerField(
        choices=Status,
        default=4,
    )
    student = models.ManyToManyField(User, null=True, blank=True, related_name='Student')
    # tutor = models.ManyToManyField(User, null=True, blank=True, related_name=_('Tutor courses'))

    def __str__(self):
        return self.program_name
class Videos(models.Model):
    program_video_name=models.ForeignKey(Program,related_name='program_video',on_delete=models.CASCADE)
    video_name=models.CharField(max_length=250)
    video_number=models.IntegerField()
    slug=models.URLField(max_length=300)
    def __str__(self):
        return self.video_name
