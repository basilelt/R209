from django.db import models

class Film(models.Model):
    titre = models.CharField(max_length=100)
    producteur = models.CharField(max_length = 100)
    acteur = models.TextField()
    date_parution = models.DateField(blank=True, null = True)
    duree = models.TimeField(auto_now=False, auto_now_add=False)
    syno = models.TextField(null = True, blank = True)
    genre = models.ForeignKey("genre", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.titre} un film {self.genre} de {self.duree} produit par {self.producteur} avec {self.acteur}, sortie le {self.date_sortie}"
        return chaine
    
    def dico(self):
        return {"titre":self.titre, "producteur":self.producteur, "acteur":self.acteur, "date_parution":self.date_parution, "duree":self.duree, "syno":self.syno, "genre":self.genre}

class Genre(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom
    
    def dico(self):
        return {"nom":self.nom, "description":self.description}