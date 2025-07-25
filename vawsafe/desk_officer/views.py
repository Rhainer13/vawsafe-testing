from django.shortcuts import render
from django.http import HttpResponse
from .forms import VictimSurvivorInformationForm, IncidentInformationForm, AllegedPerpetratorInformationForm

# Create your views here.
def index(request):
    return render(request, "desk_officer/index.html")

def victimSurvivorInformation(request):
    form = VictimSurvivorInformationForm()
    context = {
        'form': form,
    }
    return render(request, "desk_officer/registerVictim.html", context)

def incidentInformation(request):
    return render(request, "desk_officer/registerIncident.html")

def allegedPerpetratorInformation(request):
    return render(request, "desk_officer/registerPerpetrator.html")