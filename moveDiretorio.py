import shutil
def move_arquivos (caminho_antigo, caminho_novo):
    caminho_arquivo = caminho_antigo   
    caminho_destino = caminho_novo
    shutil.move(caminho_arquivo, caminho_destino)


