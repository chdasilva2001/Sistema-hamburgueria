from django.db import models

class Cliente(models.Model):     
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
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
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE, null=True, blank=True)  # Itens no pedido ou no carrinho
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    observacao = models.TextField(blank=True, null=True)
    session_id = models.CharField(max_length=40, blank=True, null=True)  # Identificador temporário

    @property
    def total(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido {self.pedido.id if self.pedido else 'Carrinho'})"


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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)  # Relaciona diretamente o cliente
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'),
                                                (4, '4 estrelas'), (5, '5 estrelas')])
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Avaliação de {self.cliente.nome} para {self.produto.nome} - Nota: {self.nota}"
