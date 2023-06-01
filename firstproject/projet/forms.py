from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'producteur', 'acteur', 'date_parution', 'duree','syno', 'genre')
        labels = {
            'titre' : _('Titre'),
            'producteur' : _('Producteur'),
            'acteur' : _('Acteur'),
            'date_parution' : _('Date de parution'),
            'duree' : _('Durée'),
            'syno' : _('Synopsis'),
            'genre' : _('Genre')
        }

class GenreForm(ModelForm):
    class Meta:
        model = models.Genre
        fields = ('nom', 'description')
        labels = {
            'nom' : _('Nom'),
            'description' : _('Description') ,
        }