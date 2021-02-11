from django.contrib import admin
from .models import Produto, Cliente, Planilha, Usuario
from django.contrib.auth import admin as auto_admin
# Register your models here.

admin.site.register(Produto)

admin.site.register(Cliente)

admin.site.register(Planilha)

admin.site.register(Usuario, auto_admin.UserAdmin)