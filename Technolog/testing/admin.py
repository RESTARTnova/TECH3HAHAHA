from django.contrib import admin
from .models import ForeignKeyTest, ForeignKeyTestF


# Register your models here.
admin.site.register(ForeignKeyTestF)
admin.site.register(ForeignKeyTest)