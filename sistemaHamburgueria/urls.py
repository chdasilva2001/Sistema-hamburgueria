from django.contrib import admin
from django.urls import path
from app1.views import Inicio, exibir_carrinho, adicionar_ao_carrinho, Adicionar_observacao, remover_do_carrinho,remover_item_do_carrinho, finalizar_pedido, CustomLoginView, CustomLogoutView, Cadastrar_usuario

app_name = "carrinho"

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', Inicio, name='inicio'),
    path("carrinho/", exibir_carrinho, name="exibir_carrinho"),  # Exibir o carrinho
    path("carrinho/adicionar/<int:produto_id>/", adicionar_ao_carrinho, name="adicionar_ao_carrinho"),  
    path("carrinho/remover/<int:item_id>/", remover_do_carrinho, name="remover_do_carrinho"), 
    path("carrinho/removeritem/<int:item_id>/", remover_item_do_carrinho, name="remover_item_do_carrinho"),  
    path("carrinho/finalizar/", finalizar_pedido, name="finalizar_pedido"), 
    path('carrinho/observacao/<int:item_id>/', Adicionar_observacao, name='adicionar_observacao'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('Cadastro/', Cadastrar_usuario, name='cadastro'),
    
    
]