from django.contrib import admin
from .models import ISQ_Questions,ISQAnswer,Initial_ISQ,Demographic_answers,Demographic_Questions,Demographic
# Register your models here.
admin.site.register(ISQ_Questions)
admin.site.register(ISQAnswer)
admin.site.register(Initial_ISQ)


admin.site.register(Demographic_Questions)
admin.site.register(Demographic)
admin.site.register(Demographic_answers)
