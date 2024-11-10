from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    assunto = models.CharField(max_length=120)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.assunto}'

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'{self.nome} - CPF: {self.cpf}'

class Estoque(models.Model):
    produto_nome = models.CharField(max_length=255)
    quantidade_disponivel = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.produto_nome

    class Meta:
        db_table = 'app_estoque'


class Pedido(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)  # Relacionado ao usuário
    data_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.cpf}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.nome_produto



