from django.contrib import admin
from .models import VictimSurvivorInformation, IncidentInformation, AllegedPerpetratorInformation 

# Register your models here.
admin.site.register(VictimSurvivorInformation)
admin.site.register(IncidentInformation)
admin.site.register(AllegedPerpetratorInformation)