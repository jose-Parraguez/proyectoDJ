from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.

def index(request):
    productos = Producto.objects.all().values() # llamar todos los productos

    print(productos)
    # productos = Producto.objects.filter(puntaje=5)#filtrar por lenguaje
    # productos = Producto.objects.get(pk = 1)#filtrar por lenguaje

    return JsonResponse(list(productos),safe= False)#json response solo toma archivos en diccionario o list
    
