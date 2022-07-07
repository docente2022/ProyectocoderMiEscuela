
from django.db import models

# Create your models here.

class escuela (models.Model):
    nombre="Escuela Intercultural Bilingüe"
    numero="807"
    domicilio="Comunidad Fortín Mbororé, Puerto Iguazú, Misiones, Argentina."
    
    
    

class Estudiante (models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField(blank=True, null=True)
    
    
class Maestros (models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField(blank=True, null=True)
    
    grado=models.PositiveIntegerField( ("Grado"))
    
class Padres(models.model):
     nombre= models.CharField(max_length=30)
     apellido= models.CharField(max_length=30)
     email= models.EmailField(blank=True, null=True)
     
     
     
####class Nosotros (models.Model)