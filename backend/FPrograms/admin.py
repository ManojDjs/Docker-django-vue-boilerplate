from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FISQ_Questions,FISQAnswer,Final_ISQ
# Register your models here.
admin.site.register(Final_ISQ)
admin.site.register(FISQ_Questions)
admin.site.register(FISQAnswer)

