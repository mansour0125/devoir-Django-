from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=100,null=True)
    prenom = models.CharField(max_length=200,null=True)
    niveau = models.CharField(max_length=200,null=True)

    
class Cour(models.Model):
    nom = models.CharField(null=True)
    date = models.DateField(auto_now_add = True,null = True)
    heure_debut= models.TimeField(auto_now_add True,null=True)
    heure_fin= models.TimeField(auto_now_add True,null=True)
    
