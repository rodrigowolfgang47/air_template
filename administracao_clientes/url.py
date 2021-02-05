from django.urls import path
from .views import meus_templates

urlpatterns =[
    path('meus_templates', meus_templates),
]