from django.db import models

# Create your models here.
class offres(models.Model):
    Poste = models.CharField(max_length=300)
    Profil = models.CharField(max_length=300)
    Compétences = models.CharField(max_length=1000)
    Qualités = models.CharField(max_length=1000)
    Contrat = models.CharField(max_length=300)
    Lieu = models.CharField(max_length=300)
    Durée = models.CharField(max_length=300)
    Démarrage = models.CharField(max_length=300)
    Expérience = models.CharField(max_length=300)

class User(models.Model):
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=200)