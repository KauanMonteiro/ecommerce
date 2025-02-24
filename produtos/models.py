from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_modified = models.DateTimeField(User, auto_now=True)
	phone = models.CharField(max_length=20, blank=True)
	old_cart = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.user.username
     
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

    post_save.connect(create_profile, sender=User)



class Cliente(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
     

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
    cliente= models.ForeignKey(Cliente,on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1, blank=True, null=True)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.produto
