from django.contrib import admin

# Register your models here.
from .models import Demographic_answers,Demographic_Questions,Demographic
admin.site.register(Demographic_Questions)
admin.site.register(Demographic)
admin.site.register(Demographic_answers)