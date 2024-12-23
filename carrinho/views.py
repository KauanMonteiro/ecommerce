from django.shortcuts import render, get_object_or_404
from .carrinho import Carrinho
from django.http import JsonResponse
from produtos.models import Produto

def resumo_carrinho(request):
    carrinho = Carrinho(request)
    quantidade = carrinho.get_quants
    produtos_carrinho = carrinho.get_prods
    return render(request,'carrinho.html',{'produtos_carrinho':produtos_carrinho,'quantidade':quantidade})

def adicionar_carrinho(request):
    carrinho = Carrinho(request) 
    if request.POST.get('action') == "post":
        produto_id = int(request.POST.get("produto_id"))
        produto_qty = int(request.POST.get('produto_qty'))

        produto= get_object_or_404(Produto, id = produto_id)

        carrinho.add(produto=produto, quantidade=produto_qty)

        carrinho_quantidade = carrinho.__len__()


        response= JsonResponse({'quant:': carrinho_quantidade})
        return response


def deletar_carrinho(request):
    pass

def atualizar_carrinho(request):
    carrinho = Carrinho(request)

    if request.POST.get('action') == "post":
        produto_id = int(request.POST.get("produto_id"))
        produto_qty = int(request.POST.get('produto_qty'))

        carrinho.atualizar(produto=produto_id,quantidade=produto_qty)

        response = JsonResponse({'quantidade':produto_qty})
        return response