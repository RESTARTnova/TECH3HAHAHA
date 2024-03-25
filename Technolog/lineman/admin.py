from django.contrib import admin

from .models import NFC, Durability, Job_titles, Logs, ReportsRoom, Users, Actions, Rooms, ActionsRoom, RoomsReport
# Register your models here.
admin.site.register(Users)
admin.site.register(Job_titles)
admin.site.register(Actions)
admin.site.register(Rooms)
admin.site.register(ActionsRoom)
admin.site.register(RoomsReport)
admin.site.register(Durability)
admin.site.register(NFC)
admin.site.register(Logs)
admin.site.register(ReportsRoom)