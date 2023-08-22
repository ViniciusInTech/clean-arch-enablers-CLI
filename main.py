import os, sys
from functions_cae import is_a_java_project, find_folder
from criarFiles import criarDir

"""def main():
    print("Bem vindo ao cae")
    if is_a_java_project():
        local_use_cases = find_folder("use_cases")
        print("o use cases está em: ", local_use_cases)
        criarDir(local_use_cases+"//teste")
    else:
        print('nenhum projeto java encontrado.')
        print('tente em um diretório válido')

if __name__ == "__main__":
    main()"""
def is_valid_args(args):
    valid_args = ["new", "function-use-case"]
    if not args:
        print('Error: args invalid. option: ', valid_args)
        return False
    for arg in args:
        if arg not in valid_args:
            print('arg: ', arg, 'Inválido')
            print('args valid: ', valid_args)
            return False
    return True
def main():
    args = sys.argv[1:]
    print('args valid:', is_valid_args(args))

if __name__ == "__main__":
    main()
