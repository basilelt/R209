from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre', 'auteur', 'date_parution', 'nombre_pages','resume', 'categorie')
        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            'date_parution' : _('Date de parution'),
            'nombre_pages' : _('Nombres de pages'),
            'resume' : _('Résumé'),
            'categorie' : _('Catégorie')
        }

class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'description')
        labels = {
            'nom' : _('Nom'),
            'description' : _('Description') ,
        }