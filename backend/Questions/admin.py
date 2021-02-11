from django.contrib import admin
from .models import Questions,Intial_BaseLine_Answer,Final_Answer,Final_Answers,Topic,Labels
# Register your models here.
admin.site.register(Topic)
admin.site.register(Questions)
admin.site.register(Intial_BaseLine_Answer)
# admin.site.register(Initial_Answers)
admin.site.register(Final_Answer)
admin.site.register(Final_Answers)
admin.site.register(Labels)

