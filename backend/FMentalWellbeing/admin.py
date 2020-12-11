from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FMWB,FMWB_answers,FMWB_Questions
# Register your models here.
admin.site.register(FMWB)
admin.site.register(FMWB_answers)
admin.site.register(FMWB_Questions)

