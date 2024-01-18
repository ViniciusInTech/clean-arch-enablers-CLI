import json
import os
import re
import subprocess
import tempfile

from cae_core.searchAndRead import find_folder
from cae_core.variables import filter_package_java, filter_java, barra_system


def split_words(string):
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+|[a-zA-Z0-9]+', string)
    return [word.lower() for word in words]


def upper_case_first(words):
    words_first_upper = []
    for word in words:
        words_first_upper.append(word.capitalize())
    return words_first_upper


def join_words(words):
    word_complete = ''
    for word in words:
        word_complete += word
    return word_complete


def to_snake_case(words):
    snake_case_string = "_".join(words).lower()
    return snake_case_string


def to_pascal_case(input_list):
    pascal_case_string = "".join(word.capitalize() for word in input_list)
    return pascal_case_string


def buscar_arquivo(nome_arquivo, diretorio=os.getcwd()):
    for pasta_atual, _, arquivos in os.walk(diretorio):
        # Procura pelo arquivo dentro da pasta atual
        if nome_arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_atual, nome_arquivo)
            with open(caminho_arquivo, 'r') as arquivo:
                return arquivo.read()
        # Procura nas pastas superiores
        diretorio_pai = os.path.dirname(pasta_atual)
        if diretorio_pai != pasta_atual:
            caminho_arquivo_pai = os.path.join(diretorio_pai, nome_arquivo)
            if os.path.exists(caminho_arquivo_pai):
                with open(caminho_arquivo_pai, 'r') as arquivo_pai:
                    return arquivo_pai.read()

    return "Arquivo não encontrado"



def extrair_ids_do_json(dados_json):
    # Carregar o JSON
    dados = json.loads(dados_json)

    # Verificar se a estrutura do JSON está correta
    if "geral" in dados and "groupId" in dados["geral"] and "artifactId" in dados["geral"]:
        group_id = dados["geral"]["groupId"]
        artifact_id = dados["geral"]["artifactId"]
        return group_id, artifact_id
    else:
        return None, None


def to_nomal_case(string):
    return string

def artifact_id(arg):
    group_id, artifact_id = extrair_ids_do_json(buscar_arquivo("configCae.json"))
    return artifact_id
def group_id(arg):
    group_id, artifact_id = extrair_ids_do_json(buscar_arquivo("configCae.json"))
    return group_id

def get_os_path(arg):
    return os.getcwd()


def to_camel_case(input_list):
    camel_case_string = "".join(word.capitalize() if index > 0 else word for index, word in enumerate(input_list))
    return camel_case_string


def to_package_format(path):
    parts = path.split(filter_package_java, filter_java)
    if len(parts) > filter_java:
        return parts[filter_java].replace(barra_system, ".")
    else:
        return path


def to_package_format_case(case):
    path = find_folder(to_snake_case(case))
    parts = path.split(filter_package_java, filter_java)
    if len(parts) > filter_java:
        return parts[filter_java].replace(barra_system, ".")
    else:
        return path


def remove_after_string(original_string, target_string):
    parts = original_string.split(target_string, 1)
    if len(parts) > 1:
        result = parts[0] + target_string
        return result
    return original_string


def remove_after_use_case(original_string):
    path_to_remove = to_package_format_case(original_string)
    target_string = "use_cases"
    return remove_after_string(path_to_remove, target_string)


def remove_blank_lines(lines_list):
    non_blank_lines = [line.strip() for line in lines_list if line.strip()]
    return non_blank_lines


def filtrar_itens(lista, palavras_chave):
    itens_filtrados = [item for item in lista if any(palavra.lower() in item.lower() for palavra in palavras_chave)]
    return itens_filtrados

def open_in_nano():
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
        temp_file.write(b"")
        temp_file_name = temp_file.name
    try:
        subprocess.call(["notepad", temp_file_name])
    except FileNotFoundError:
        print("Please install nano or use a different text editor.")
        return None
    with open(temp_file_name, "r") as edited_file:
        edited_content = edited_file.read()

    return edited_content