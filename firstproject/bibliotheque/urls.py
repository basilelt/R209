from django.urls import path
from . import views, categorie_views

urlpatterns = [
    # patterns for books
    path('home/', views.home),
    path('livre/index/', views.index),
    path('livre/ajout/', views.ajout),
    path('livre/traitement/', views.traitement), # ajouter la route traitement associé à l'action traitement du fichier views.py
    path('livre/all/', views.all),
    path('livre/affiche/<int:id>/', views.affiche), # ajouter la route traitement associé à l'action traitement du fichier views.py.
                                                    # bien faire attention qu'il n'y ai pas d'espace dans les balises <>,
                                                    # sinon cela génère une erreur.
    path('livre/update/<int:id>/', views.update),
    path('livre/traitementupdate/<int:id>/',views.traitementupdate),
    path('livre/delete/<int:id>/', views.delete),

    # patterns for categories
    path('categorie/index/', categorie_views.index),
    path('categorie/ajout/', categorie_views.ajout),
    path('categorie/traitement/', categorie_views.traitement),
    path('categorie/all/', categorie_views.all),
    path('categorie/affiche/<int:id>/', categorie_views.affiche),
    path('categorie/update/<int:id>/', categorie_views.update),
    path('categorie/traitementupdate/<int:id>/', categorie_views.traitementupdate),
    path('categorie/delete/<int:id>/', categorie_views.delete),
]
