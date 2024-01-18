import os
import sys


def check_for_none(value, error_message="Erro: Ocorreu um erro, finalizando."):
    if value is None:
        print(error_message)
        sys.exit(1)

def function_dir_dont_found(value, name_dir):
    check_for_none(value,f"Error: dir {name_dir} não encontrada no template")

def dont_find_use_cases_dir(value):
    message = f"pasta use_cases não encontrada em nenhum lugar de {os.getcwd()}"
    check_for_none(value, message)
