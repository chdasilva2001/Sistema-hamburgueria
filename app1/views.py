from django.shortcuts import render

# Create your views here.

def Inicio(request):
    return render(request,'Inicio.html')


def Pedido(request):
    return render(request,'Pedido.html')
