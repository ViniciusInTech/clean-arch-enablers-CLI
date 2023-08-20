import os
from functions_cae import is_a_java_project


def main():
    print("Bem vindo ao cae")
    if is_a_java_project():
        print('foi detectado um projeto java')
    else:
        print('nenhum projeto java encontrado.')
        print('tente em um diretório válido')

if __name__ == "__main__":
    main()