from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement), # ajouter la route traitement associé à l'action traitement du fichier views.py
    path('all/', views.all),
    path('affiche/<int:id>/',views.affiche), # ajouter la route traitement associé à l'action traitement du fichier views.py.
                                             # bien faire attention qu'il n'y ai pas d'espace dans les balises <>,
                                             # sinon cela génère une erreur.
    path('update/<int:id>/',views.update),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path('delete/<int:id>/',views.delete),
]
