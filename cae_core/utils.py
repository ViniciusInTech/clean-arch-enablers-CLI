import os
import re
import subprocess
import tempfile

from cae_core.searchAndRead import find_folder
from cae_core.variables import filter_package_java, filter_java


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

def get_os_path(arg):
    return os.getcwd()


def to_camel_case(input_list):
    camel_case_string = "".join(word.capitalize() if index > 0 else word for index, word in enumerate(input_list))
    return camel_case_string


def to_package_format(path):
    parts = path.split(filter_package_java, filter_java)
    if len(parts) > filter_java:
        return parts[filter_java].replace("\\", ".")
    else:
        return path


def to_package_format_case(case):
    path = find_folder(to_snake_case(case))
    parts = path.split(filter_package_java, filter_java)
    if len(parts) > filter_java:
        return parts[filter_java].replace("\\", ".")
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