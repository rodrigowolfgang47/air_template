from django.urls import path
from .views import meus_templates, deletar_cliente

urlpatterns =[
    path('meus_templates', meus_templates, name='meus_templates'),
    path('deletar/<str:cliente>', deletar_cliente, name='deletar' )
]