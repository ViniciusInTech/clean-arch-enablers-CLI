import os

from utils import join_words, to_package_format, to_pascal_case, to_snake_case, split_words, remove_after_string, \
    find_folder
from variables import write_permission, dir_to_be_created, file_to_be_created





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
    path_use_case = create_dir(find_folder("use_cases") + "\\" + to_snake_case(name_folder))
    for case in folder_structure:
        create_dir(path_use_case + "\\" + case)


def create_files_structure(name_file):
    name_file = split_words(name_file)
    path_use_case_file = find_folder(to_snake_case(name_file))
    name_file_pascal_case = to_pascal_case(name_file)

    updated_file_to_be_created = [file.replace("case_name", name_file_pascal_case) for file in file_to_be_created]
    for file in updated_file_to_be_created:
        path_file = path_use_case_file + "\\" + file
        create_file(path_file, name_file)

def make_path_format(name_file, path):
    path_use_case_file = find_folder(to_snake_case(name_file))