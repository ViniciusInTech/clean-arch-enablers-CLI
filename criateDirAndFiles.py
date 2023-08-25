import os

from findDir import find_folder
from utils import join_words, to_package_format, to_pascal_case, to_snake_case
from variables import write_permission, use_case, dir_to_be_created


def createDir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"create use-case in: {path}")
        return path
    else:
        print(f'don´t possible create use-case in: {path}')


def create_folder_structure(name):
    use_cases = find_folder(use_case)
    path_use_case = createDir(use_cases + "\\" + to_snake_case(name))
    for case in dir_to_be_created:
        createDir(path_use_case + "\\" + case)


def create_use_case_fuc(name, path):
    new_file = os.path.join(path, name + ".java")
    name = to_pascal_case(name)
    package = to_package_format(path)
    with open(new_file, write_permission) as file:
        file.write(f"package {package}; \n")
        file.write(f"public abstract class {name} extends FunctionUseCase<,> {{\n")
        file.write(f"protected {name}() {{ \n")
        file.write(f"super(); \n")
        file.write(f"}} \n")
        file.write(f"}} \n")
