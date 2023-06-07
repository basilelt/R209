from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class VoitureForm(ModelForm):
    class Meta:
        model = models.Voiture
        fields = ("modele",
                  "marque",
                  "achat", 
                  "place", 
                  "description", 
                  "longueur", 
                  "climatisation")
        labels = {
            'modele' : _('Modèle'),
            'marque' : _('Marque'),
            'achat' : _("Date d'Achat") ,
            'place' : _('Nombre de Places'),
            'description' : _('Description'),
            'longueur' : _('Longueur (m)'),
            'climatisation' : _('Climatisation ?')
        }
        