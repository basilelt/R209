from django.shortcuts import render
from .forms import CategorieForm
from . import models
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'bibliotheque/categorie/index.html')

def ajout(request):
    if request.method == "POST":
        form = CategorieForm(request)
        if form.is_valid():
            categorie = form.save()
            return render(request,"bibliotheque/categorie/affiche.html",{"categorie" : categorie})
        else:
            return render(request,"bibliotheque/categorie/ajout.html",{"form": form})
    else :
        form = CategorieForm()
        return render(request,"bibliotheque/categorie/ajout.html",{"form" : form})
    
# Get data from formulaire
def traitement(request):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save()
        return render(request,"bibliotheque/categorie/affiche.html",{"categorie" : categorie})
    else:
        return render(request,"bibliotheque/categorie/ajout.html",{"form": cform})

def all(request):
    all = list(models.Categorie.objects.all())
    return render(request,"bibliotheque/categorie/all.html",{"all": all})

def affiche(request, id):
    livre = models.Categorie.objects.get(pk=id)
    return render(request,"bibliotheque/categorie/affiche.html",{"livre": livre})

def update(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    dictionnaire = {'nom':categorie.nom, 'description':categorie.description}
    cform = CategorieForm(dictionnaire) 
    return render(request,"bibliotheque/categorie/update.html",{"form": cform, "categorie": categorie})

def traitementupdate(request, id):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save(commit=False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/bibliotheque/categorie/all")
    else:
        return render(request, "bibliotheque/categorie/update.html", {"form": cform, "id": id})
    
def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/bibliotheque/categorie/all")