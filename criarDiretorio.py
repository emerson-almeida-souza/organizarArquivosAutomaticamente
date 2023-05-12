import os
path = r'C:\Users\emerson\Downloads'
def criarDiretorio(nome_diretorio, path):
    diretorio = nome_diretorio
    # verificando se o diretório já existe
    if not os.path.exists(f'{path}/{diretorio}'):
    # criando um novo diretório
        os.mkdir(f'{path}/{diretorio}')
        print(f"O diretório {diretorio} foi criado com sucesso!")
    else:
        print(f"O diretório {diretorio} já existe!")

criarDiretorio('xls', path)


    



