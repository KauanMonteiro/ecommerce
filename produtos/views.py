from django.shortcuts import render
from .models import Produto,Categoria

def home(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request,'pages/home.html',{'produto':produto,'categoria':categoria})