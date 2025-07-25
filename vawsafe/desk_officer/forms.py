from django.forms import ModelForm
from .models import VictimSurvivorInformation, IncidentInformation, AllegedPerpetratorInformation

class VictimSurvivorInformationForm(ModelForm):
    class Meta:
        model = VictimSurvivorInformation
        fields = '__all__'

class IncidentInformationForm(ModelForm):
    class Meta:
        model = IncidentInformation
        fields = '__all__'

class AllegedPerpetratorInformationForm(ModelForm):
    class Meta:
        model = AllegedPerpetratorInformation
        fields = '__all__'