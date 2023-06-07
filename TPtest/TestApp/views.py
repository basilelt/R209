from django.shortcuts import render
from .forms import VoitureForm
from . import models
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'testapp/index.html')

def voitures(request):
    all = list(models.Voiture.objects.all())
    return render(request,"testapp/liste_voitures.html",{"all": all})

def ajouter_voiture(request):
    if request.method == "POST":
        vform = VoitureForm(request)
        if vform.is_valid():
            voiture = vform.save()
            return render(request,"testapp/afficher_voiture.html",{"voiture" : voiture})
        else:
            return render(request,"testapp/ajouter_voiture.html",{"form": vform})
    else :
        vform = VoitureForm() # création d'un formulaire vide
        return render(request,"testapp/ajouter_voiture.html",{"form" : vform})

def traitement(request):
    vform = VoitureForm(request.POST)
    if vform.is_valid():
        voiture = vform.save()
        return render(request,"testapp/afficher_voiture.html",{"voiture" : voiture})
    else:
        return render(request,"testapp/ajouter_voiture.html",{"form": vform})
    
def afficher_voiture(request, id):
    voiture = models.Voiture.objects.get(pk=id)
    return render(request,"testapp/afficher_voiture.html",{"voiture": voiture})

def modifier_voiture(request, id):
    voiture = models.Voiture.objects.get(pk=id)
    dictionnaire = voiture.dico
    vform = VoitureForm(dictionnaire) 
    return render(request,"testapp/modifier_voiture.html",{"form": vform, "voiture": voiture})

def traitementupdate(request, id):
    vform = VoitureForm(request.POST)
    if vform.is_valid():
        voiture = vform.save(commit=False)
        voiture.id = id
        voiture.save()
        return HttpResponseRedirect(f"/testapp/afficher_voiture/{id}")
    else:
        return render(request, "testapp/modifier_voiture.html", {"form": vform, "id": id})

def supprimer_voiture(id):
    voiture = models.Voiture.objects.get(pk=id)
    voiture.delete()
    return HttpResponseRedirect("/testapp/voitures")
