from django.db import models

class Assinatura(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='assinaturas/')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome