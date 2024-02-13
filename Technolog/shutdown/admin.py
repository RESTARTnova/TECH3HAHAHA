from django.contrib import admin
from .models import TypeShutdown, FactorShutdown, ClassShutdown,Shutdown
# Register your models here.
admin.site.register(TypeShutdown),
admin.site.register(FactorShutdown),
admin.site.register(ClassShutdown),
admin.site.register(Shutdown),
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()