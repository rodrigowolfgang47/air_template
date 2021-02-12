from django.db import models
from django.contrib.auth.models import AbstractUser
from air_template.settings import AUTH_USER_MODEL

class Usuario(AbstractUser):
    UF_CHOICES = (
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
    )

    celular = models.CharField(max_length=11)
    estado = models.CharField(max_length=20, choices=UF_CHOICES)

class Planilha(models.Model):
    cliente = models.CharField(max_length=100, blank=False, null=False)
    documento = models.FileField(upload_to='media/%Y/%m/%d/')
    subido_as = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cliente} {self.documento} {self.subido_as}'


class Cliente(models.Model):
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=50, null=False, primary_key=True, blank=False)
    criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cliente} {self.criacao}'


class Produto(models.Model):
    cliente = models.ForeignKey('Cliente', blank=False, on_delete=models.CASCADE, null=False)
    cod_da_peca = models.CharField(max_length=20, blank=False)
    marca = models.CharField(max_length=100, blank=False)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    aplicacao = models.CharField(max_length=150, blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    destaque = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.cliente} {self.cod_da_peca}'