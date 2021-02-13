from django.urls import path, include
from .views import meus_templates, deletar_cliente, meu_cliente, template_estatico

urlpatterns =[
    path('meus_templates/', meus_templates, name='templates'),
    path('deletar/<str:cliente>', deletar_cliente, name='deletar' ),
    path('meus_templates/<str:cliente>/', meu_cliente, name='meucliente'),
    path('meus_templates/<str:cliente>/<str:user>/estatico/', template_estatico, name='estatico'),
]