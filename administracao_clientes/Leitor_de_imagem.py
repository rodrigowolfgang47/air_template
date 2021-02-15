import os


def leitor_de_imagens(cod_da_peca):
    caminho = 'C:/Users/rodri/OneDrive/Área de Trabalho/img/pecas'

    lista_de_imagens = os.listdir(caminho)

    for i in range(len(lista_de_imagens)):
        lista_de_imagens[i] = lista_de_imagens[i].lower()
        lista_de_imagens[i] = lista_de_imagens[i].replace('.jpg', '')

    return cod_da_peca in lista_sem_jpg
