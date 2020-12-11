from django.contrib import admin

# Register your models here.
from .models import WBMNU_answers,WBMNU_Questions,WBMNU
admin.site.register(WBMNU)
admin.site.register(WBMNU_Questions)
admin.site.register(WBMNU_answers)
