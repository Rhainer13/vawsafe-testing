from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_victim/', views.registerVictim, name='register_victim'),
]