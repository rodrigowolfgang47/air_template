from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
import mimetypes
import pandas as pd
from .forms import PlanilhaForm
from .models import Produto


# Create your views here.

# Coloquei o decorator login_request para obrigar o usuário a logar
@login_required()
def crie_seu_template(request):
    form = PlanilhaForm()
    return render(request, 'crie_seu_template.html', {'form': form})


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

    # Adicionei a lib pandas para abrir a planilha e a openpyxl para gerenciar os arquivos em excel
    file = pd.read_excel(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; file_name=%s" % file_name
    return response


def leitor_de_planilha(planilha):
    date_frame = pd.read_excel(planilha, index_col=None, header=None)

    armazena_cod = []

    # pega a primeira coluna inteita
    colunas = date_frame[0]
    linhas_por_linha = 1

    for cod in colunas:
        while linhas_por_linha <= len(colunas) - 1:
            codigo_da_peca = colunas[linhas_por_linha]
            linhas_por_linha += 1
            armazena_cod.append(codigo_da_peca)

    # ------------------------------------------------ #

    # titulo da planilha começa aqui

    lista_de_dicionario = []

    titulo_da_planilha = date_frame.loc[0]

    todos_os_cod = date_frame[0]

    for codigos in range(1, len(todos_os_cod) - 1):
        dicionario_com_itens = {}
        linhas = date_frame.loc[codigos]
        comeca_na_primeira_coluna = 0

        for titulo in titulo_da_planilha:
            dicionario_com_itens[titulo_da_planilha[comeca_na_primeira_coluna]] = linhas[comeca_na_primeira_coluna]
            comeca_na_primeira_coluna += 1

        lista_de_dicionario.append(dicionario_com_itens)

    return lista_de_dicionario


def subir_para_model(lista_de_produtos, cliente):
    for itens in lista_de_produtos:
        produtos = Produto.objects.create(
            cliente=cliente,
            cod_da_peca=itens['Cód. Cobra'],
            marca=itens['Marca'],
            descricao=itens['Descrição de produto'],
            aplicacao=itens['Aplicação'],
            preco=itens['Preço'],
            destaque=itens['Gostaria de destacar este produto?'],
        )
        produtos.save()

    return produtos


# pega upload de arquivos
def upload_files(request):
    if request.method == 'POST':
        # Instansiando o formulário
        form = PlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            nome_do_arquivo = form.save(commit=False)
            # form.save()
            url_do_arquivo_na_pasta = nome_do_arquivo.documento

            # funcao que le os dados da planilha e retorna um dicionario
            dicionario_com_dados = leitor_de_planilha(url_do_arquivo_na_pasta)

            cliente = request.POST.get('cliente')

            subir_para_model(dicionario_com_dados, cliente)

            return redirect('template')
    else:
        form = PlanilhaForm()
    return render(request, 'crie_seu_template.html', {'form': form})


def template_final(request):
    produtos = Produto.objects.all()
    print(produtos)
    return render(request, 'template_final.html',{'produtos': produtos})
