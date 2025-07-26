from django.forms import ModelForm
from .models import VictimSurvivorInformation, IncidentInformation, AllegedPerpetratorInformation

class VictimSurvivorInformationForm(ModelForm):
    class Meta:
        model = VictimSurvivorInformation
        fields = '__all__'

class IncidentInformationForm(ModelForm):
    class Meta:
        model = IncidentInformation
        exclude = ['victimSurvivor']

class AllegedPerpetratorInformationForm(ModelForm):
    class Meta:
        model = AllegedPerpetratorInformation
        exclude = ['victimSurvivor']
