from django.contrib import admin
from .models import Produto, Cliente, Planilha
# Register your models here.

admin.site.register(Produto)

admin.site.register(Cliente)

admin.site.register(Planilha)