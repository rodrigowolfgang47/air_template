from django.urls import path
from .views import cadastro, activation_sent_view, activate

urlpatterns =[
    path('cadastro/', cadastro, name="cadastro"),
    path('sent/', activation_sent_view, name='ativador_enviado'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]