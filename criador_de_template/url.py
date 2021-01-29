from django.urls import path
from .views import crie_seu_template, sair, download_file, upload_files

urlpatterns = [
    path('crie_seu_template/', crie_seu_template, name='cria-template'),
    path('logout/', sair, name='sair'),
    path('staticfiles/excel/base_air_template_layout.xlsx', download_file, name='download'),
    path('upload/', upload_files, name='upload')
]