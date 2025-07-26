from django.shortcuts import render
from django.http import HttpResponse
from .forms import VictimSurvivorInformationForm, IncidentInformationForm, AllegedPerpetratorInformationForm

def index(request):
    return render(request, "desk_officer/index.html")

def registerVictim(request):
    if request.method == 'POST':
        victim_form = VictimSurvivorInformationForm(request.POST)
        incident_form = IncidentInformationForm(request.POST)
        perpetrator_form = AllegedPerpetratorInformationForm(request.POST)

        if victim_form.is_valid() and incident_form.is_valid() and perpetrator_form.is_valid():
            victim = victim_form.save()

            incident = incident_form.save(commit=False)
            incident.victimSurvivor = victim
            incident.save()

            perpetrator = perpetrator_form.save(commit=False)
            perpetrator.victimSurvivor = victim
            perpetrator.save()

            return HttpResponse("Victim registered successfully.")
    else:
        victim_form = VictimSurvivorInformationForm()
        incident_form = IncidentInformationForm()
        perpetrator_form = AllegedPerpetratorInformationForm()

    return render(request, "desk_officer/register_victim.html", {
        'victim_form': victim_form,
        'incident_form': incident_form,
        'perpetrator_form': perpetrator_form
    })
