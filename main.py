import os
from getExtensao import retornaExtensao
from criarDiretorio import criarDiretorio
from moveDiretorio import move_arquivos

PATH = r'C:\Users\user\Downloads' #Aqui você coloca o caminho da pasta
todos_arquivos = os.listdir(PATH)
caminho_atual_arquivo = None
caminho_novo = None
extensao = None
novo_caminho = None

for arquivo in todos_arquivos:
    caminho_atual_arquivo = f'{PATH}\{arquivo}'

    if os.path.isfile(caminho_atual_arquivo):
        extensao = retornaExtensao(arquivo)
        criarDiretorio(extensao, PATH)
        
        novo_caminho= f'{PATH}\{extensao}\{arquivo}'
        move_arquivos(caminho_atual_arquivo, novo_caminho)

