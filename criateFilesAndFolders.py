import os
import re

from searchAndRead import read_file_txt, list_files_on_folder, find_folder
from utils import to_snake_case, split_words, remove_blank_lines, join_words, to_pascal_case, to_package_format_case, \
    remove_after_use_case
from variables import write_permission, dir_of_config, structure_root_folder, \
    name_of_file_structure_dir, regex_to_replace_template, file_folder_name

string_manipulation = {"case_name_pascal_case": to_pascal_case,
                       "case_name_snake_case": to_snake_case,
                       "package": to_package_format_case,
                       "package_no_use_case": remove_after_use_case}


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"create use-case in: {path}")
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
    path_use_case = create_dir(find_folder(structure_root_folder) + "\\" + to_snake_case(name_folder))
    for case in folder_structure:
        create_dir(path_use_case + "\\" + case)


def create_dir_structure(function):
    list_to_add_structure = []
    structures = remove_blank_lines(read_file_txt(dir_of_config+"\\"+function+name_of_file_structure_dir))
    for structure in structures:
        list_to_add_structure.append(structure)
    print(list_to_add_structure)
    return list_to_add_structure


def replace_text_template(list_of_strings, substitution_dictionary, name_case):
    for i, linha in enumerate(list_of_strings):
        matches = re.findall(regex_to_replace_template, linha)
        for match in matches:
            if match in substitution_dictionary:
                replacement_func = substitution_dictionary[match]
                replaced_text = re.sub(regex_to_replace_template, lambda x: replacement_func(name_case), linha, count=1)
                linha = replaced_text
        list_of_strings[i] = linha
    return list_of_strings


def create_file_structure(function, name_case):
    name_case = split_words(name_case)
    path_of_file = dir_of_config+"\\"+function+file_folder_name
    list_of_files = list_files_on_folder(path_of_file)
    path_of_case = find_folder(structure_root_folder)
    for file in list_of_files:
        conteudo_file = read_file_txt(path_of_file+"\\"+file)
        content = remove_blank_lines(replace_text_template(conteudo_file, string_manipulation, name_case))
        create_file(path_of_case+"\\"+content[1]+"\\"+content[0], join_words(conteudo_file[2:]))
        print("file created " + content[0])
