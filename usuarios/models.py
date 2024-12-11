from django.db import models

ADMINISTRADOR = 'Admin'
COMUM='Comum'

CARGO_CHOICES = [
    (ADMINISTRADOR, 'Administrador'),
    (COMUM,'Comum')
]

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=64)
    telefone = models.CharField(max_length=50)
    cargo = models.CharField(max_length=18, choices=CARGO_CHOICES, default=COMUM)

    def __str__(self):
        return self.nome
    