from django.shortcuts import render
from .forms import LivreForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'bibliotheque/index.html')

def ajout(request):
    if request.method == "POST":    # Arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données.
                                    # Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données.
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"bibliotheque/affiche.html",{"livre" : livre}) # Envoie vers une page d'affichage du livre créé
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"bibliotheque/ajout.html",{"form" : form})
    
# Get data from formulaire
def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})

def all(request):
    all = list(models.Livre.objects.all())
    return render(request,"bibliotheque/all.html",{"all": all})

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"bibliotheque/affiche.html",{"livre": livre})

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    dictionnaire = {'titre':livre.titre, 'auteur':livre.auteur, 'date_parution':livre.date_parution, 'nombre_pages':livre.nombre_pages,'resume':livre.nombre_pages}
    lform = LivreForm(dictionnaire) 
    return render(request,"bibliotheque/update.html",{"form": lform, "livre": livre})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False) # création d'un objet livre avec les données du formulaire mais sans l'enregistrer dans la base.
        livre.id = id; # modification de l'id de l'objet
        livre.save() # mise à jour dans la base puisque l'id du livre existe déja.
        return HttpResponseRedirect("/bibliotheque/all") # plutot que d'avoir un gabarit pour nous indiquer que cela c'est bien passé,
                                                      # nous repartons sur une autre actionqui renvoie vers la page d'index de notre
                                                      # site (celle avec la liste des entrées)
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})
    
def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/bibliotheque/all")