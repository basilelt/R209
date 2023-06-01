from django.shortcuts import render
from .forms import FilmForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'projet/home.html')

def index(request):
    return render(request, 'projet/film/index.html')

def ajout(request):
    if request.method == "POST":
        form = FilmForm(request)
        if form.is_valid():
            film = form.save()
            return render(request,"projet/film/affiche.html",{"film" : film})
        else:
            return render(request,"projet/film/ajout.html",{"form": form})
    else :
        form = FilmForm()
        return render(request,"projet/film/ajout.html",{"form" : form})
    
# Get data from formulaire
def traitement(request):
    fform = FilmForm(request.POST)
    if fform.is_valid():
        film = fform.save()
        return render(request,"projet/film/affiche.html",{"film" : film})
    else:
        return render(request,"projet/film/ajout.html",{"form": fform})

def all(request):
    all = list(models.Film.objects.all())
    return render(request,"projet/film/all.html",{"all": all})

def affiche(request, id):
    film = models.Film.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"projet/film/affiche.html",{"film": film})

def update(request, id):
    film = models.Film.objects.get(pk=id)
    dictionnaire = film.dico
    fform = FilmForm(dictionnaire) 
    return render(request,"projet/film/update.html",{"form": fform, "film": film})

def traitementupdate(request, id):
    fform = FilmForm(request.POST)
    if fform.is_valid():
        film = fform.save(commit=False)
        film.id = id
        film.save()
        return HttpResponseRedirect("/projet/film/all")
    else:
        return render(request, "projet/film/update.html", {"form": fform, "id": id})
    
def delete(request, id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/projet/film/all")