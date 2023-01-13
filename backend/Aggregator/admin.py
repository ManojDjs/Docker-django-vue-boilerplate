from django.contrib import admin
from .models import Course,Sites,Team,Testmonials

# Register your models here.
admin.site.register(Course)
admin.site.register(Sites)
admin.site.register(Team)
admin.site.register(Testmonials)