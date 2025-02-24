from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Produto,Categoria
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def home(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request,'pages/home.html',{'produto':produto,'categoria':categoria})

def vermaisproduto(request, id):
    produto = Produto.objects.get(pk=id)
    categoria = produto.categoria
    produtos_relacionados = Produto.objects.filter(categoria=categoria).exclude(pk=id)
    return render(request,'pages/vermaisproduto.html',{'produto':produto,'produtos_relacionados': produtos_relacionados})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request,username=username,password=senha)
        if user is not None:
            login(request,user)
            return redirect(reverse('home'))
        else:
            return render(request,"pages/login.html")
    return render(request,"pages/login.html",{})

def logout_user(request):
    request.session.flush()
    return redirect(reverse('home'))

def register_user(request):
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            
            user = authenticate(username=username,password=password)

            login(request,user)

            return redirect("home")

    return render(request,"pages/cadastro.html",{"form":form})

def update_password(request):
    pass

def update_user(request):
    pass

def update_info(request):
    pass