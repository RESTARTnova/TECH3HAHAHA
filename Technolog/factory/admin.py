from django.contrib import admin
from .models import Factoryes, Departaments, Aggregates, Machines, Nodes, Elements, Details
# Register your models here.
admin.site.register(Factoryes)
admin.site.register(Departaments)
admin.site.register(Aggregates)
admin.site.register(Machines)
admin.site.register(Nodes)
admin.site.register(Elements)
admin.site.register(Details)
# admin.site.register(Faults)