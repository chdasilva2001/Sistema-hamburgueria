from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Produto, Pedido, ItemPedido, Cliente



def Inicio(request):
    produtos = Produto.objects.all() 

    paginator = Paginator(produtos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Inicio.html', {'page_obj': page_obj} )

def Login(request):
    return render(request, "Login.html")

def Cadastro(request):
    return render(request, "Cadastro.html")

def pedido(request):
    return render(request, "Pedido.html")


def adicionar_ao_carrinho(request, produto_id): 
    produto = get_object_or_404(Produto, id=produto_id)

    session_id = request.session.session_key
    if not session_id: 
        request.session.create()
        session_id = request.session.session_key

    item, created = ItemPedido.objects.get_or_create(
        session_id = session_id, 
        produto = produto, 
        pedido__isnull=True, 
        defaults={
            'quantidade': 1, 
            'preco_unitario': produto.preco,
        }
    )

    if not created: 
        item.quantidade += 1 
        item.save()

    return JsonResponse({'mensagem': 'Produto adicionado ao carrinho!', 'quantidade': item.quantidade})


def exibir_carrinho(request):
    session_id = request.session.session_key
    if not session_id:
        return render(request, 'carrinho.html', {'itens': []})

    itens = ItemPedido.objects.filter(session_id=session_id, pedido__isnull=True)
    total = sum(item.total for item in itens)

    return render(request, 'carrinho.html', {'itens': itens, 'total': total})



def finalizar_pedido(request): 
    if request.method == 'POST': 
        cliente = get_object_or_404(Cliente, id= request.POST.get("cliente_id"))

        pedido = Pedido.objects.create(cliente=cliente)

        session_id = request.session.session_key
        itens = ItemPedido.objects.filter(session_id=session_id, pedido__isnull=True)

        for item in itens: 
            item.pedido = pedido 
            item.session_id = none 
            item.save()


            itens.delete()



            return redirect('whatsapp')
