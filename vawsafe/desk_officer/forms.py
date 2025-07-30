from django.forms import ModelForm
from .models import VictimSurvivorInformation, IncidentInformation, AllegedPerpetratorInformation
from django import forms

class VictimSurvivorInformationForm(ModelForm):
    class Meta:
        model = VictimSurvivorInformation
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class IncidentInformationForm(ModelForm):
    class Meta:
        model = IncidentInformation
        exclude = ['victim_survivor']

class AllegedPerpetratorInformationForm(ModelForm):
    class Meta:
        model = AllegedPerpetratorInformation
        exclude = ['victim_survivor']
