from django.db import models


# Create your models here.

class Parent(models.Model):
    nomComplet = models.CharField(max_length=30, null=False)
    cnie = models.CharField(max_length=15, null=False)
    etatFamilial = models.CharField(max_length=30, null=False)
    tailleMenage = models.CharField(max_length=20, null=False)
    habitat = models.CharField(max_length=200, null=False)
    adresse = models.CharField(max_length=200, null=False)
    tel = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Enfant(models.Model):
    GENDER_CHOICES = (
        ('garçon', 'garçon'),
        ('fille', 'fille'),
    )
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='enfants')

    genre = models.CharField(max_length=20, null=False, choices=GENDER_CHOICES)
    age = models.IntegerField(null=False, default=0)
    etablissement = models.CharField(max_length=40)
    nScol = models.CharField(max_length=40, null=False)
