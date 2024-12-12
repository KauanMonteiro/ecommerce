from django.shortcuts import render
from .models import Produto,Categoria

def home(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request,'pages/home.html',{'produto':produto,'categoria':categoria})

def vermaisproduto(request, id):
    produto = Produto.objects.get(pk=id)
    categoria = produto.categoria
    produtos_relacionados = Produto.objects.filter(categoria=categoria).exclude(pk=id)
    return render(request,'pages/vermaisproduto.html',{'produto':produto,'produtos_relacionados': produtos_relacionados})