import os
import re
import json

from cae_plugins.db import get_function_by_name
from cae_core.searchAndRead import find_folder
from cae_core.utils import to_snake_case, split_words, join_words, to_pascal_case, to_package_format_case, \
    remove_after_use_case, get_os_path, to_nomal_case
from cae_core.variables import write_permission, structure_root_folder, \
    regex_to_replace_template, barra_system

string_manipulation = {
    "pc": to_pascal_case,
    "sc": to_snake_case,
    "pk": to_package_format_case,
    "pk_no_name": remove_after_use_case,
    "os": get_os_path,
    "group_id": to_nomal_case,
    "artifact_id": to_nomal_case,
}


def criar_novo_project_config(group_id, artifact_id, pasta):
    # Construindo o caminho do arquivo JSON
    caminho_arquivo = os.path.join(pasta, 'configCae.json')

    # Criando o dicionário com os dados groupId e artifactId
    dados = {
        "geral": {
            "groupId": group_id,
            "artifactId": artifact_id
        }
    }

    # Escrevendo os dados no arquivo JSON
    with open(caminho_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
    print(f"Arquivo config criado em {caminho_arquivo}")
    return caminho_arquivo

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"create dir: {path}")
        return path
    else:
        print(f'don´t possible create use-case in: {path}')


def create_file(path, conteudo):
    if os.path.exists(path):
        print(f"file already exists in directory: {path}")
    else:
        with open(path, write_permission) as file:
            file.write(conteudo)


def create_folder_structure(name_folder, folder_structure):
    name_folder = split_words(name_folder)
    path_use_case = create_dir(find_folder(structure_root_folder) + barra_system + to_snake_case(name_folder))
    for case in folder_structure:
        create_dir(path_use_case + barra_system + case)


def replace_text_in_string(input_string, substitution_dictionary, name_case):
    matches = re.findall(regex_to_replace_template, input_string)

    for tag, content in matches:
        if content.lower() == "<name>" and tag in substitution_dictionary:
            replacement_func = substitution_dictionary[tag]
            replacement = replacement_func(name_case)
            input_string = input_string.replace(f"<{tag}>{content}</{tag}>", replacement)
        elif tag in substitution_dictionary:
            replacement_func = substitution_dictionary[tag]
            replacement = replacement_func(name_case)
            input_string = input_string.replace(f"<{tag}>{content}</{tag}>", replacement)

    return input_string


def replace_tag(content, name):
    return replace_text_in_string(content, string_manipulation, name)


def create_file_structure(name_case, function):
    name_case = split_words(name_case)
    function_obj = get_function_by_name(function)
    files_to_be_created = function_obj.GetFiles()
    path_of_case = find_folder(structure_root_folder)
    if path_of_case is None:
        path_of_case = os.getcwd()

    for file in files_to_be_created:
        content = replace_tag(file.GetContent(), name_case)
        path_of_file = replace_tag(file.GetPath(), name_case)
        name_of_file = replace_tag(file.GetName(), name_case)
        create_file(path_of_case+barra_system+path_of_file+barra_system+name_of_file, join_words(content))
        print(f"file created '{name_of_file}' in {path_of_file}")


def mudar_diretorio(caminho):
    try:
        os.chdir(caminho)
        print(f"Diretório alterado para: {os.getcwd()}")
    except FileNotFoundError:
        print("Caminho não encontrado.")
    except Exception as e:
        print(f"Erro ao tentar mudar o diretório: {e}")