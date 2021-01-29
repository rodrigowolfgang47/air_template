from django.db import models


class Planilha(models.Model):
    cliente = models.CharField(max_length=50, blank=True)
    documento = models.FileField(upload_to='media/%Y/%m/%d/')
    subido_as = models.DateTimeField(auto_now=True)
