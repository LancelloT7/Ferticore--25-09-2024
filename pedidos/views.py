from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pedido
from produtos.models import Produto



def cadPedidos(request):
    produtos = Produto.objects.all()  # Busque todos os produtos
    print(produtos)
    if request.method == "GET":
        return render (request, 'cad_pedidos.html', {'produtos': produtos})
    elif request.method == "POST":
        
        nome_cliente = request.POST.get('nome_cliente')
        produto_id = request.POST.get('produto')
        produto = Produto.objects.get(id=produto_id)  # Recupera o produto pelo ID

        pedido = Pedido(nome_cliente=nome_cliente, produto=produto)
        pedido.save()
        return HttpResponse('Pedido cadastrado com sucesso!')
    redirect ('inicio.html')





# Create your views here.
