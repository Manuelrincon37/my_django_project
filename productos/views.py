from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto
# Create your views here.

# /productos/


def index(request):
    productos = Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )
