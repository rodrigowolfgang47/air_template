from django.db import models


class Planilha(models.Model):
    cliente = models.CharField(max_length=50, blank=True)
    documento = models.FileField(upload_to='media/%Y/%m/%d/')
    subido_as = models.DateTimeField(auto_now=True)


class Produto(models.Model):
    cliente = models.CharField(max_length=50, blank=True)
    cod_da_peca = models.CharField(max_length=10, blank=True)
    marca = models.CharField(max_length=20, blank=True)
    descricao = models.CharField(max_length=150, blank=True)
    aplicacao = models.CharField(max_length=150, blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return Produto
