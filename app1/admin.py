from django.contrib import admin
from .models import Produto, Pedido, ItemPedido, Entrega, Avaliacao

# Registro de Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')  # Exibe essas colunas na listagem
    search_fields = ('nome',)  # Permite pesquisar pelo nome do produto

admin.site.register(Produto, ProdutoAdmin)

# Registro de ItemPedido
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1  # Número de linhas extras para adicionar novos itens diretamente no pedido

# Registro de Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente', 'status', 'data_pedido')  # Exibe essas colunas na listagem
    list_filter = ('status', 'data_pedido')  # Filtros para status e data do pedido
    search_fields = ('nome_cliente', 'telefone_cliente')  # Permite pesquisar pelo nome do cliente ou telefone
    inlines = [ItemPedidoInline]  # Exibe os itens do pedido diretamente na página de detalhes do pedido

admin.site.register(Pedido, PedidoAdmin)

# Registro de Entrega
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'endereco', 'status')  # Exibe essas colunas na listagem
    list_filter = ('status',)  # Filtro para status de entrega

admin.site.register(Entrega, EntregaAdmin)

# Registro de Avaliação
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'comentario', 'nota')  # Exibe essas colunas na listagem
    search_fields = ('cliente__nome', 'produto__nome')  # Permite pesquisar pelo nome do cliente ou do produto
    list_filter = ('nota',)  # Filtro para a nota da avaliação

admin.site.register(Avaliacao, AvaliacaoAdmin)
