from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def cadProduto(request):
    if request.method == "GET":
        return render(request, 'cadProduto.html')
    elif request.method == "POST":
        
        nome = request.POST.get('nome')
        produto = Produto(nome=nome)
        produto.save()
        print('cadastrado')
        return HttpResponse('Produto cadastrado')
