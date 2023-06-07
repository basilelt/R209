from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('voitures/', views.voitures),
    path('ajouter_voiture/', views.ajouter_voiture),
    path('traitement/', views.traitement),
    path('afficher_voiture/<int:id>/', views.afficher_voiture),
    path('modifier_voiture/<int:id>/', views.modifier_voiture),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path('supprimer_voiture/<int:id>/', views.supprimer_voiture),
]
