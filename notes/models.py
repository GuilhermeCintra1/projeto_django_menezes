from django.db import models

class Cavalo(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.CharField('idade em anos', max_length=200)
    pai = models.CharField(max_length=200)
    mae = models.CharField('mãe', max_length=200)
    proprietario = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.nome
