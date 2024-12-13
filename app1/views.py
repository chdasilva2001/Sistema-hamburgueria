from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Produto, Pedido, ItemPedido, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView



def Inicio(request):
    produtos = Produto.objects.all() 

    paginator = Paginator(produtos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Inicio.html', {'page_obj': page_obj} )

def Cadastrar_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')  # Redireciona após cadastro
    else:
        form = UserCreationForm()
    return render(request, 'Cadastro.html', {'form': form})


# Login - Usando a view do Django
class CustomLoginView(LoginView):
    template_name = 'Login.html'

# Logout - Usando a view do Django
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redireciona para a página inicial após o logout


@login_required
def adicionar_ao_carrinho(request, produto_id): 
    
    produto = get_object_or_404(Produto, id=produto_id)


    item = ItemPedido.objects.filter(usuario = request.user, produto=produto, pedido__isnull=True).first()

    if item: 
        item.quantidade += 1 
        item.save()
        messages.success(request, "Produto adicionado ao carrinho")
    else: 
        ItemPedido.objects.create(usuario = request.user, produto = produto, quantidade = 1, preco_unitario = produto.preco)
        messages.success(request, "Produto adicionado ao carrinho")

    return redirect("exibir_carrinho") 
    
@login_required
def exibir_carrinho(request):
    itens = ItemPedido.objects.filter(usuario = request.user, pedido__isnull=True)
    total = sum(item.total for item in itens)

    return render(request, 'carrinho.html', {'itens': itens, 'total': total})


@login_required
def remover_do_carrinho(request, item_id): 
    item = get_object_or_404(ItemPedido, id=item_id, usuario=request.user, pedido__isnull=True)
    item.delete()

    messages.success(request, "Produto removido com sucesso")

    return redirect("exibir_carrinho")

@login_required
def remover_item_do_carrinho(request, item_id): 
    item = get_object_or_404(ItemPedido, id=item_id, usuario=request.user, pedido__isnull=True)
    

    if item: 
        item.quantidade -= 1 
        item.save()

    messages.success(request, "Produto removido com sucesso")

    return redirect("exibir_carrinho")


@login_required
def finalizar_pedido(request): 
    itens_carrinho = ItemPedido.objects.filter(usuario=request.user, pedido__isnull=True)
    
    
    if not itens_carrinho.exists(): 
        messages.error(request, "seu carrinho está vazio. ")
        return redirect("exibir_carrinho")

    pedido = Pedido.objects.create(usuario=request.user, status="Pendente", total = 0)

 
    for item in itens_carrinho: 
        item.pedido = pedido
        item.save()

    pedido.total = sum(item.total for item in itens_carrinho)
    pedido.save()


    messages.success(request, "Pedido finalizado com sucesso!")
    return redirect("inicio")




@login_required
def Adicionar_observacao(request, item_id):
    if request.method == "POST":
        observacao = request.POST.get("observacao", "")
        item = get_object_or_404(ItemPedido, id=item_id)

        # Atualiza a observação
        item.observacao = observacao
        item.save()

        messages.success(request, "Observação adicionada com sucesso!")
        return redirect("exibir_carrinho")  # Redireciona para a página do carrinho
    else:
        messages.error(request, "Método inválido para adicionar observação.")
        return redirect("exibir_carrinho")