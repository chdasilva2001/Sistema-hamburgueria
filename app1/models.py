from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    telefone_cliente = models.CharField(max_length=15)
    endereco_cliente = models.CharField(max_length=255)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Recebido', 'Recebido'),
            ('Em preparo', 'Em preparo'),
            ('Em entrega', 'Em entrega'),
            ('Concluído', 'Concluído'),
        ],
        default='Recebido'
    )

    def __str__(self):
        return f"Pedido {self.id} - {self.nome_cliente}"
    


class ItemPedido(models.Model):
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE)  # Relaciona com Pedido
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)  # Relaciona com Produto
    quantidade = models.PositiveIntegerField(default=1)  # Quantidade do produto no pedido
    observacao = models.TextField(blank=True, null=True)  # Observações opcionais para o item

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido {self.pedido.id})"


# Modelo para Entrega
class Entrega(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)  # Um pedido tem uma entrega associada
    endereco = models.CharField(max_length=255) 
    status = models.CharField(max_length=50, choices=[('Em andamento', 'Em andamento'), 
                                                      ('Entregue', 'Entregue'), 
                                                      ('Cancelado', 'Cancelado')],
                              default='Em andamento')

    def __str__(self):
        return f"Entrega do pedido {self.pedido.id} - Status: {self.status}"


# Modelo para Avaliação
class Avaliacao(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Cada avaliação está ligada a um pedido
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Cada avaliação é para um produto específico
    nota = models.PositiveIntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'),
                                                (4, '4 estrelas'), (5, '5 estrelas')])
    comentario = models.TextField(blank=True, null=True)  # Comentário opcional

    def __str__(self):
        return f"Avaliação de {self.cliente.nome} para {self.produto.nome} - Nota: {self.nota}"
