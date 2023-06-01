from django.urls import path
from . import views, genre_views

urlpatterns = [
    # patterns for films
    path('home/', views.home),
    path('film/index/', views.index),
    path('film/ajout/', views.ajout),
    path('film/traitement/', views.traitement), # ajouter la route traitement associé à l'action traitement du fichier views.py
    path('film/all/', views.all),
    path('film/affiche/<int:id>/', views.affiche), # ajouter la route traitement associé à l'action traitement du fichier views.py.
                                                    # bien faire attention qu'il n'y ai pas d'espace dans les balises <>,
                                                    # sinon cela génère une erreur.
    path('film/update/<int:id>/', views.update),
    path('film/traitementupdate/<int:id>/',views.traitementupdate),
    path('film/delete/<int:id>/', views.delete),

    # patterns for genre
    path('genre/index/', genre_views.index),
    path('genre/ajout/', genre_views.ajout),
    path('genre/traitement/', genre_views.traitement),
    path('genre/all/', genre_views.all),
    path('genre/affiche/<int:id>/', genre_views.affiche),
    path('genre/update/<int:id>/', genre_views.update),
    path('genre/traitementupdate/<int:id>/', genre_views.traitementupdate),
    path('genre/delete/<int:id>/', genre_views.delete),
]
