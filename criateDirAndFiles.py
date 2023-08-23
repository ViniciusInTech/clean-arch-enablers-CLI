import os

def criarDir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f'Caso de uso criada em {path}')
    else:
        print(f'Caso de uso já existe em {path}')