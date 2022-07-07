from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse ( "Esta es la Pagina de Inicio")

def escuela (request):
    return HttpResponse ("acá va estar la informacion general de la institución")
def estudiantes(request):
    return HttpResponse ("acá habrá materiales de estudio para los niños")
def maestros(request):
    return HttpResponse ("acá los maestros podran encontrar informacion, calendario, subir info, hacer posteos en la vista estudiantes")
def padres(request): 
    return HttpResponse ("acá los padres podran leer info sobre las actividades desarrolladas en la escuela, seccion noticias")