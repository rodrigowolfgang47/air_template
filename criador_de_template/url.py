from django.urls import path
from .views import crie_seu_template, sair

urlpatterns = [
    path('crie_seu_template/', crie_seu_template, name='cria-template'),
    path('logout/', sair, name='sair')
]