from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Produto



def Inicio(request):
    produtos = Produto.objects.all() 

    paginator = Paginator(produtos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Inicio.html', {'page_obj': page_obj} )

def Pedido(request):
    return render(request, "Pedido.html")

def Login(request):
    return render(request, "Login.html")

def Cadastro(request):
    return render(request, "Cadastro.html")


