from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import VictimSurvivorInformation, IncidentInformation, AllegedPerpetratorInformation
from .forms import VictimSurvivorInformationForm, IncidentInformationForm, AllegedPerpetratorInformationForm

def index(request):
    return render(request, "desk_officer/index.html")

def dashboard(request):
    return render(request, "desk_officer/dashboard.html")

def registerVictim(request):
    if request.method == 'POST':
        victim_form = VictimSurvivorInformationForm(request.POST)
        incident_form = IncidentInformationForm(request.POST)
        perpetrator_form = AllegedPerpetratorInformationForm(request.POST)

        if victim_form.is_valid() and incident_form.is_valid() and perpetrator_form.is_valid():
            victim = victim_form.save()

            incident = incident_form.save(commit=False)
            incident.victim_survivor = victim
            incident.save()

            perpetrator = perpetrator_form.save(commit=False)
            perpetrator.victim_survivor = victim
            perpetrator.save()

            return redirect('victim_list')  # Redirect to the victim list after saving
    else:
        victim_form = VictimSurvivorInformationForm()
        incident_form = IncidentInformationForm()
        perpetrator_form = AllegedPerpetratorInformationForm()

    return render(request, "desk_officer/register-victim.html", {
        'victim_form': victim_form,
        'incident_form': incident_form,
        'perpetrator_form': perpetrator_form
    })

def victimList(request):
    victims = VictimSurvivorInformation.objects.all()
    return render(request, "desk_officer/victim-list.html", {'victims': victims})