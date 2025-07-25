from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('victim_survivor_information/', views.victimSurvivorInformation, name='victim_survivor_information'),
]