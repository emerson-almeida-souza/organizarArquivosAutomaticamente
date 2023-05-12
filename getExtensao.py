import os

def retornaExtensao (arquivo):
    tamanho_arquivo = len(arquivo) - 1
    
    while tamanho_arquivo > -1:
        indice_do_ponto = None
        if arquivo[tamanho_arquivo] == '.':
            indice_do_ponto = tamanho_arquivo + 1   #ACHEI O PONTO
            break
        tamanho_arquivo -= 1
    
    extensao = arquivo[indice_do_ponto:len(arquivo)]
    return extensao







    
