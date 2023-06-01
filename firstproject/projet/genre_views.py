from django.shortcuts import render
from .forms import GenreForm
from . import models
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'projet/genre/index.html')

def ajout(request):
    if request.method == "POST":
        form = GenreForm(request)
        if form.is_valid():
            genre = form.save()
            return render(request,"projet/genre/affiche.html",{"genre" : genre})
        else:
            return render(request,"projet/genre/ajout.html",{"form": form})
    else :
        form = GenreForm()
        return render(request,"projet/genre/ajout.html",{"form" : form})
    
# Get data from formulaire
def traitement(request):
    cform = GenreForm(request.POST)
    if cform.is_valid():
        genre = cform.save()
        return render(request,"projet/genre/affiche.html",{"genre" : genre})
    else:
        return render(request,"projet/genre/ajout.html",{"form": cform})

def all(request):
    all = list(models.Genre.objects.all())
    return render(request,"projet/genre/all.html",{"all": all})

def affiche(request, id):
    genre = models.Genre.objects.get(pk=id)
    return render(request,"projet/genre/affiche.html",{"genre": genre})

def update(request, id):
    genre = models.Genre.objects.get(pk=id)
    dictionnaire = {'nom':genre.nom, 'description':genre.description}
    gform = GenreForm(dictionnaire) 
    return render(request,"projet/genre/update.html",{"form": gform, "genre": genre})

def traitementupdate(request, id):
    cform = GenreForm(request.POST)
    if cform.is_valid():
        genre = cform.save(commit=False)
        genre.id = id
        genre.save()
        return HttpResponseRedirect("/projet/genre/all")
    else:
        return render(request, "projet/genre/update.html", {"form": cform, "id": id})
    
def delete(request, id):
    genre = models.Genre.objects.get(pk=id)
    genre.delete()
    return HttpResponseRedirect("/projet/genre/all")