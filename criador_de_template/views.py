from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mimetypes
import pandas as pd


# Create your views here.

# Coloquei o decorator login_request para obrigar o usuário a logar
@login_required()
def crie_seu_template(request):
    return render(request, 'crie_seu_template.html')


# View responsável por deslogar usuário
def sair(request):
    # pego a request e passo para o logout
    if request.method == 'POST':
        logout(request)
        return redirect('home')


# View responsável por gerar o download
def download_file(request):
    file_path = "criador_de_template/staticfiles/excel/base_air_template_layout.xlsx"
    file_name = 'base_air_template_layout.xlsx'

    # Adicionei a lib pandas para abrir a planilha e a openpyxl para erencias os arquivos em excel
    file = pd.read_excel(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; file_name=%s" % file_name
    return response


def leitor_de_planilha(planilha):
    arquivo = planilha
    date_frame = pd.read_excel(arquivo, index_col=None, header=None)

    armazena_dados = {}
    armazena_linha = {}

    # Conta o numero de colunas
    numero_de_linhas = len(date_frame.loc[0])

    colunas = date_frame[0]

    # Contador de informações
    index_pra_baixo = 1
    index_pra_frente = 1
    index_pra_titulo = 0

    # vai iterar o valor de colunas contido no data frame
    for coluna_01 in date_frame:

        # vai adicionar o codigo da primeira linha da primeira coluna
        cod_da_peca = colunas[index_pra_baixo]
        codigo_da_peca_str = str(cod_da_peca)

        # vai iterar em todos os itens da linha e adicionar a lista Armazena_Linha
        while index_pra_frente < numero_de_linhas:
            # Le a a primeira linha do data frame
            titulo_da_linha = date_frame.loc[0]

            # Le a coluna depois do código
            coluna = date_frame.loc[index_pra_baixo]

            # Adiciona o titulo como key e a celula como valor
            armazena_linha[titulo_da_linha[index_pra_frente]] = coluna[index_pra_frente]

            index_pra_frente += 1
            index_pra_titulo += 1

        # armazena o código do produto como key e a linha completa com titulos para cada campo
        armazena_dados[codigo_da_peca_str] = armazena_linha

        index_pra_baixo += 1

    return armazena_dados
