from django.db import models
from django.contrib.auth.models import User

    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("Pendente", "Pendente"), ("Concluído", "Concluído"), ("Cancelado", "Cancelado")],
        default="Pendente"
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Pedido {self.id} ({self.usuario.username}) - {self.status}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        "Pedido", on_delete=models.CASCADE, null=True, blank=True, related_name="itens"
    )  # Associado ao pedido, se finalizado
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Vinculado ao usuário
    quantidade = models.PositiveIntegerField(default=1)  # Sempre positiva
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    observacao = models.TextField(blank=True, null=True)  # Ex.: "Sem cebola"
    
    @property
    def total(self):
        return self.quantidade * self.preco_unitario  # Calcula o preço total

    def __str__(self):
        if self.pedido:
            return f"{self.quantidade}x {self.produto.nome} (Pedido {self.pedido.id})"
        return f"{self.quantidade}x {self.produto.nome} (Carrinho do usuário {self.usuario.username})"

    class Sem_duplicatas:
        unique_together = ("usuario", "produto", "pedido") 



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
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'),
                                                (4, '4 estrelas'), (5, '5 estrelas')])
    comentario = models.TextField(blank=True, null=True)

