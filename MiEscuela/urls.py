from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='index'),
    
    path('escuela/', escuela),
    
    path('estudiantes/',estudiantes),
    
    path('maestros/', maestros ),
    
    path('padres/', padres),
    
]