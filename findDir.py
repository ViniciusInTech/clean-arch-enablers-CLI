import os
import re

from criateDirAndFiles import create_file
from utils import to_pascal_case, to_snake_case, split_words, find_folder, join_words, to_package_format_case, \
    remove_after_use_case

dir_of_code = os.path.dirname(os.path.abspath(__file__))
dir_of_config = dir_of_code + "\\config\\functions"

string_manipulation = {"case_name_pascal_case": to_pascal_case,
                       "case_name_snake_case": to_snake_case,
                       "package": to_package_format_case,
                       "package_no_use_case": remove_after_use_case}



def filter_dir_and_files(path):
    content = os.listdir(path)
    folders = []
    files = []

    for item in content:
        
        if os.path.isdir(os.path.join(path, item)):
            folders.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)

    return folders, files


def list_dir_on_folder(path):
    try:
        folders, _ = filter_dir_and_files(path)

        return folders

    except OSError as e:
        print(f"nada encontrado no dir: {e}")
        return []


def list_files_on_folder(path):
    try:
        _, files = filter_dir_and_files(path)
        return files

    except OSError as e:
        print(f"Error ao listar files: {e}")


def read_file_txt(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"The file {path} dont´t find.")
        return []


def remove_blank_lines(lines_list):
    non_blank_lines = [line.strip() for line in lines_list if line.strip()]
    return non_blank_lines


def structure_dir_function(function):
    list_to_add_structure = []
    structures = remove_blank_lines(read_file_txt(dir_of_config+"\\"+function+"\\dir_structure.txt"))
    for structure in structures:
        list_to_add_structure.append(structure)
    print(list_to_add_structure)
    return list_to_add_structure


def replace_text(list_of_strings, substitution_dictionary, name_case):
    standard = r"<<(.*?)>>"
    for i, linha in enumerate(list_of_strings):
        matches = re.findall(standard, linha)
        for match in matches:
            if match in substitution_dictionary:
                replacement_func = substitution_dictionary[match]
                replaced_text = re.sub(standard, lambda x: replacement_func(name_case), linha, count=1)
                linha = replaced_text  # Atualiza a linha com a substituição
        list_of_strings[i] = linha  # Atualiza a linha na lista

    return list_of_strings


def structure_file_functions(function, name_case):
    name_case = split_words(name_case)
    path_of_file = dir_of_config+"\\"+function+"\\files"
    list_of_files = list_files_on_folder(path_of_file)
    path_of_case = find_folder("use_cases")
    for file in list_of_files:
        conteudo_file = read_file_txt(path_of_file+"\\"+file)
        content = remove_blank_lines(replace_text(conteudo_file, string_manipulation, name_case))
        create_file(path_of_case+"\\"+content[1]+"\\"+content[0], join_words(conteudo_file[2:]))
        print("file created " + content[0])
