from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dahsboard/', views.dashboard, name='dashboard'),
    path('register_victim/', views.registerVictim, name='register_victim'),
    path('victims/', views.victimList, name='victim_list'),
]