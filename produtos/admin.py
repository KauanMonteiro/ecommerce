from django.contrib import admin
from .models import Pedido,Produto,Categoria

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Categoria)