from django.shortcuts import render
from .models import Produto

def home(request):
    produto = Produto.objects.all()
    return render(request,'pages/home.html',{'produto':produto})