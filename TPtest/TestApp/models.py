from django.db import models

class Voiture(models.Model): 
    modele = models.CharField(max_length=20)
    marque = models.CharField(max_length = 20)
    achat = models.DateField(blank=True, null = True)
    place = models.IntegerField()
    description = models.TextField(null = True, blank = True, max_length=300)
    longueur = models.FloatField()
    climatisation = models.BooleanField()

    def __str__(self):
        if self.climatisation:
            chaine = f"{self.modele} de la marque {self.marque} a la climatisation"
        else:
            chaine = f"{self.modele} de la marque {self.marque} n'a pas la climatisation"
        return chaine
    
    def dico(self):
        return {"modele":self.modele, 
                "marque":self.marque, 
                "achat":self.achat, 
                "place":self.place, 
                "description":self.description, 
                "longueur":self.longueur, 
                "climatisation":self.climatisation}
