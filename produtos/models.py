from django.db import models
from usuarios.models import Usuario
import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=65, blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=80, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    capa = models.ImageField(upload_to='capa/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    quantidade = models.IntegerField(default=1, blank=True, null=True)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.produto
