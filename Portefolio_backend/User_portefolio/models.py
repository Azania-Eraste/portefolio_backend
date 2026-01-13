from django.db import models
from django.contrib.auth.models import AbstractUser



class Utilisateur(AbstractUser):

    photo_profil = models.TextField()
    description = models.TextField(null=True)
    age = models.TextField(null=True)
    lien_cv = models.TextField(max_length=500, blank=True)
    telephone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Projet(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='projets')
    titre = models.CharField(max_length=200)
    resume = models.TextField()
    image = models.TextField()
    lien = models.TextField(max_length=500)

    def __str__(self):
        return self.titre
    
class Experience(models.Model):
    Utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='experiences')
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=100)
    nom_entreprise = models.CharField(max_length=100)
    description = models.TextField()
    type_de_contrat = models.CharField(max_length=50)

class Localisation(models.Model):
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    quartier = models.CharField(max_length=100)

class Service(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='services', null=True)
    localisation = models.OneToOneField(Localisation, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=100)
    detail = models.TextField()
    type_de_service = models.CharField(max_length=100)
    outils = models.CharField(max_length=200) 

class ReseauSocial(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='reseaux')
    nom_plateforme = models.CharField(max_length=50)
    lien = models.TextField()

class PriseDeContact(models.Model):
    nom_complet = models.CharField(max_length=200)
    objet = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField()
    date_envoi = models.DateTimeField(auto_now_add=True)