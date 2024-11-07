from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    assunto = models.CharField(max_length=120)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.assunto}'
