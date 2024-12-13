from django.contrib import admin
from .models import Produto, Pedido, ItemPedido, Entrega, Avaliacao





# Registro de Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')  # Exibe essas colunas na listagem
    search_fields = ('nome',)  # Permite pesquisar pelo nome do produto

admin.site.register(Produto, ProdutoAdmin)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1  # Número de linhas extras para adicionar itens ao pedido
    readonly_fields = ('produto', 'quantidade', 'preco_unitario', 'total',)  # Campos que serão somente leitura
    can_delete = True  # Permite excluir os itens
    show_change_link = True  # Exibe um link para editar os itens

# Registro de Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'data_criacao', 'total')  # Exibe as colunas
    list_filter = ('status', 'data_criacao')  # Filtros para status e data do pedido
    search_fields = ('cliente__nome', 'cliente__telefone')  # Permite pesquisar pelo nome ou telefone do cliente
    inlines = [ItemPedidoInline]  # Exibe os itens do pedido diretamente na página de detalhes do pedido
    ordering = ('-data_criacao',)  # Ordena os pedidos pela data, do mais recente para o mais antigo

    # Método para calcular o total do pedido
    def total_pedido(self, obj):
        return sum(item.total for item in obj.itens.all())  # Soma o total de todos os itens do pedido
    total_pedido.admin_order_field = 'id'  # Permite ordenar pela coluna total_pedido no admin
    total_pedido.short_description = 'Total'  # Descrição da coluna

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
