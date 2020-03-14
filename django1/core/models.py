from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preco',max_digits=8,decimal_places=2)
    estoque = models.IntegerField('Qtde estoque')


class Cliente(models.Model):
    nome = models.CharField('Nome',max_length=100)
    sobrenome = models.CharField('Sobrenome',max_length=100)
    idade = models.IntegerField('Idade')
    email=models.EmailField('E-mail',max_length=100)


