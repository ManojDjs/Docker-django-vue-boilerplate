from django.contrib import admin

# Register your models here.
from .models import MWB,MWB_answers,MWB_Questions
admin.site.register(MWB_Questions)
admin.site.register(MWB_answers)
admin.site.register(MWB)
