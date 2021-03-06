from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mimetypes
import pandas as pd
from .forms import PlanilhaForm
from .models import Produto, Cliente
from django.db import IntegrityError
from django.contrib import messages
import os


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
# não estou mais utilizando esta view
def download_file(request):
    file_path = "criador_de_template/static/excel/base_air_template_layout.xlsx"
    file_name = 'base_air_template_layout.xlsx'

    # Adicionei a lib pandas para abrir a planilha e a openpyxl para gerenciar os arquivos em excel
    file = pd.read_excel(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; file_name=%s" % file_name
    return response


# responsavel por ler a planilha que foi enviada
def leitor_de_planilha(request, planilha):
    date_frame = pd.read_excel(planilha, index_col=None, header=None)
    # titulo da planilha começa aqui
    date_frame.fillna('-', inplace=True)
    lista_de_dicionario = []

    # pega a primeira linha da planilha
    titulo_da_planilha = date_frame.loc[0]

    todos_os_cod = date_frame[0]

    for codigos in range(1, len(todos_os_cod)):
        dicionario_com_itens = {}
        linhas = date_frame.loc[codigos]
        comeca_na_primeira_coluna = 0

        for titulo in titulo_da_planilha:
            titulo_da_coluna = titulo_da_planilha[comeca_na_primeira_coluna]
            linhas_da_coluna = linhas[comeca_na_primeira_coluna]

            dicionario_com_itens[titulo_da_coluna] = linhas_da_coluna

            comeca_na_primeira_coluna += 1

        lista_de_dicionario.append(dicionario_com_itens)

    for itens in lista_de_dicionario:
        itens['Cód. Cobra'] = itens['Cód. Cobra'].upper()
        itens['Marca'] = itens['Marca'].lower()
        try:
            itens['Preço'] = float(itens['Preço'])
        except:
            continue

    for itens in lista_de_dicionario:
        eh_float = isinstance(itens['Preço'], float)
        aplicacao_eh_float = isinstance(itens['Aplicação'], float)

        print(eh_float)
        print(f'Preço:{itens["Preço"]}')

        if itens['Marca'] == "-":
            mensagem = messages.error(request, 'O campo de marca não pode estar em branco, verifique a planilha')
            return mensagem

        elif not eh_float:
            mensagem = messages.error(request, 'O valor do preço deve ser numério')
            return mensagem


    return lista_de_dicionario


# Verifica se há fotos na pasta
def leitor_de_imagens(cod_da_peca):
    caminho = 'static/img/pecas_logos'

    lista_de_imagens = os.listdir(caminho)

    for i in range(len(lista_de_imagens)):
        lista_de_imagens[i] = lista_de_imagens[i].upper()
        lista_de_imagens[i] = lista_de_imagens[i].replace('.JPG', '')

    return cod_da_peca in lista_de_imagens


# Sobe para model a planilha lida
def subir_para_model(request, lista_de_produtos, nome_cliente):
    try:
        cliente = Cliente.objects.create(
            cliente=nome_cliente,
            usuario=request.user
        )

        if cliente:
            for itens in lista_de_produtos:
                codigo = itens['Cód. Cobra']

                tem_foto = leitor_de_imagens(str(codigo))

                if tem_foto:
                    Produto.objects.create(
                        cliente=cliente,
                        cod_da_peca=itens['Cód. Cobra'],
                        marca=itens['Marca'],
                        descricao=itens['Descrição de produto'],
                        aplicacao=itens['Aplicação'],
                        preco=itens['Preço'],
                        destaque=itens['Gostaria de destacar este produto?'],
                        imagem=itens['Cód. Cobra']
                    )
                else:
                    Produto.objects.create(
                        cliente=cliente,
                        cod_da_peca=itens['Cód. Cobra'],
                        marca=itens['Marca'],
                        descricao=itens['Descrição de produto'],
                        aplicacao=itens['Aplicação'],
                        preco=itens['Preço'],
                        destaque=itens['Gostaria de destacar este produto?'],
                        imagem=itens['Marca']
                    )

    except IntegrityError:
        mensagem = messages.error(request, 'O cliente já existe na sua lista.')
        return mensagem

    return nome_cliente


# pega upload de arquivos e envia planilha pa model
@login_required()
def upload_files(request):
    if request.method == 'POST':
        # Instansiando o formulário
        form = PlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            nome_do_arquivo = form.save(commit=False)
            # form.save()
            url_do_arquivo_na_pasta = nome_do_arquivo.documento

            # funcao que le os dados da planilha e retorna um dicionario
            dicionario_com_dados = leitor_de_planilha(request,url_do_arquivo_na_pasta)

            if dicionario_com_dados == None:
                return redirect('cria-template')

            cliente = request.POST.get('cliente')

            retorno = subir_para_model(request, dicionario_com_dados, cliente)

            if retorno == None:
                return redirect('cria-template')
            else:
                cliente = Cliente.objects.get(cliente=cliente)
                produtos = cliente.produto_set.all()

                return render(request, 'template_final.html', {'produtos': produtos})
    else:
        form = PlanilhaForm()
    return render(request, 'crie_seu_template.html', {'form': form})