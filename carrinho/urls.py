from django.urls import path
from . import views

urlpatterns = [
    path('', views.resumo_carrinho, name="resumo_carrinho"),
    path('add/', views.adicionar_carrinho, name="adicionar_carrinho"),
    path('delete/', views.deletar_carrinho, name="deletar_carrinho"),
    path('update/', views.atualizar_carrinho, name="atualizar_carrinho"),
]
