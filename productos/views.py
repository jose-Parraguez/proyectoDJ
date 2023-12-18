from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.

def index(request):
    productos = Producto.objects.all() # llamar todos los productos

    return render(
        request,
        'index.html',
        context ={'productos':productos}
    )

def detalle(request,producto_id):

    producto = get_object_or_404(Producto, id= producto_id)
    producto = Producto.objects.get(id = producto_id)# asi se obtiene el dato de producto

    return render (request,'detalle.html',context={ 'producto': producto})
    