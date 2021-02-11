from django.contrib import admin
from .models import Course,Video,Week,Dairy,Enrolled,DairyLabel

# Register your models here.
admin.site.register(Course)
admin.site.register(Week)
admin.site.register(Video)
admin.site.register(Dairy)
admin.site.register(Enrolled)
admin.site.register(DairyLabel)
