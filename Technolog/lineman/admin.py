from django.contrib import admin

from .models import Bypass, Job_titles, Reports, Systems, Users
# Register your models here.
admin.site.register(Users)
admin.site.register(Systems)
admin.site.register(Bypass)
admin.site.register(Reports)
admin.site.register(Job_titles)