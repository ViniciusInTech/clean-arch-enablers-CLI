import os

from content_fuc import fuc_content_case, fuc_content_factory, fuc_content_wrapper
from findDir import find_folder
from utils import join_words, to_package_format, to_pascal_case, to_snake_case, split_words, remove_after_string
from variables import write_permission, use_case, dir_to_be_created, file_to_be_created




content_mapping = {
    "case": fuc_content_case,
    "factory": fuc_content_factory,
    "wrapper": fuc_content_wrapper
}

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"create use-case in: {path}")
        return path
    else:
        print(f'don´t possible create use-case in: {path}')


def create_file(path, name_file):
    if os.path.exists(path):
        print(f"file already exists in directory: {path}")
    else:
        with open(path, write_permission) as file:
            content = content_mapping.get(split_words(path)[-2])
            if callable(content):
                file.write(content(path, name_file))
            else:
                print("não foi possível achar conteudo")


def create_folder_structure(name):
    name = split_words(name)
    path_use_case = create_dir(use_case + "\\" + to_snake_case(name))
    for case in dir_to_be_created:
        create_dir(path_use_case + "\\" + case)


def create_files_structure(name_file):
    name_file = split_words(name_file)
    path_use_case_file = find_folder(to_snake_case(name_file))
    name_file_pascal_case = to_pascal_case(name_file)

    updated_file_to_be_created = [file.replace("case_name", name_file_pascal_case) for file in file_to_be_created]
    for file in updated_file_to_be_created:
        path_file = path_use_case_file + "\\" + file
        create_file(path_file, name_file)
