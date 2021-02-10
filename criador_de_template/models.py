from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    pass

class Planilha(models.Model):
    cliente = models.CharField(max_length=50, blank=True)
    documento = models.FileField(upload_to='media/%Y/%m/%d/')
    subido_as = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cliente} {self.documento} {self.subido_as}'


class Cliente(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cliente = models.CharField(max_length=50, null=False, primary_key=True, blank=False)
    criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cliente} {self.criacao}'


class Produto(models.Model):
    cliente = models.ForeignKey('Cliente', blank=False, on_delete=models.CASCADE, null=False)
    cod_da_peca = models.CharField(max_length=10, blank=False)
    marca = models.CharField(max_length=20, blank=False)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    aplicacao = models.CharField(max_length=150, blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    destaque = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.cliente} {self.cod_da_peca}'