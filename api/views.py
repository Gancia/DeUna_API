from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def home(request):
    return render(request, 'index.html')  # Se asume que 'index.html' está en api/templates

def index(request):
    return render(request, 'index.html')
