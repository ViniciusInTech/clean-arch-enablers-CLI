import os
import sys

from cae_core.authCae import is_valid_args, is_a_java_project
from cae_core.createProject import create_dir_structure_pk, create_maven_project, create_project_pk
from cae_core.searchAndRead import list_dir_on_folder, find_folder, find_folder_absolute, find_files_by_name
from cae_core.utils import open_in_nano, filtrar_itens, split_words, to_camel_case, to_pascal_case, clean_project, \
    install_project
from cae_plugins.db import *
from cae_core.criateFilesAndFolders import create_folder_structure, create_file_structure, mudar_diretorio, \
    criar_novo_project_config
from cae_plugins.template_commands_json import new_file_json, new_function_json
from cae_core.variables import ignore_the_first_arg, arg_index_of_use_case_name, arg_function_index, function_index, \
    barra_system


def main():
    args = sys.argv[ignore_the_first_arg:]
    if is_valid_args(args):
        options_functions[args[function_index]](args)
    else:
        print("invalid arguments")


def ci_all(args):
    ci = args[function_index]
    all = args[arg_function_index]
    if ci == "-ci" and all == "-all":
        paths = find_files_by_name("pom.xml")
        for path in paths:
            clean_project(path)
            install_project(path)


def new(args):
    function = args[arg_function_index]
    if function.lower() == "project":
        arg_list = []
        arg = args[arg_index_of_use_case_name].lower()
        arg_list.append(arg)
        group_id = args[arg_index_of_use_case_name+1]
        create_dir_structure_pk(arg)
        name_dir = to_pascal_case(split_words(arg))
        criar_novo_project_config(group_id, arg, f"{os.getcwd()}{barra_system}{name_dir}")
        mudar_diretorio(f"{os.getcwd()}{barra_system}{name_dir}")
        create_file_structure(arg, args[1])
        create_project_pk(group_id, arg_list, function.lower())
    if function.lower() == "rest-api":
        arg = args[arg_index_of_use_case_name].lower()
        arg_list_ = [arg]
        group_id = args[arg_index_of_use_case_name + 1]
        create_project_pk(group_id, arg_list_,function.lower())
    else:
        arg = args[arg_index_of_use_case_name]
        arg_function_name = args[arg_function_index]
        dir_root = os.getcwd()
        itens = filtrar_itens(list_dir_on_folder(os.getcwd()), ['Adaptadores', 'Core', "Montadores"])
        for i in itens:
            mudar_diretorio(find_folder_absolute(i))
            dir_structure = get_dir_by_function(f"{arg_function_name}_" + i)
            create_folder_structure(arg, dir_structure)
            create_file_structure(arg, f"{arg_function_name}_" + i)
            mudar_diretorio(dir_root)


def add(args):
    names = [args[1]]
    print(f"You are about to create a new template '{args[1]}'")
    print(f"Press ENTER to exit")
    names = name_add(names)
    dirs = dir_add()
    files = file_add()
    template_json = new_function_json(names, dirs, files)
    save_new_function(template_json, names[0])


def name_add(names):
    print(" ")
    print("Template ID:")
    while True:
        name = input("name: ")
        if name == "":
            break
        names.append(name)
    return names


def dir_add():
    dirs = []
    print(" ")
    print("Dir to be created in this template: ")
    while True:
        dir = input("dir ")
        if dir == "":
            break
        dirs.append(dir)
    return dirs


def file_add():
    files = []
    print(" ")
    print("Files to be created in this template: ")
    while True:
        name = input("name of file: ")
        if name == "":
            break
        path = input("Relative path of file: ")
        input("Press any key to open content template editor")
        content = open_in_nano()
        files.append(new_file_json(name, path, content))
    return files


options_functions = {
    "new": new,
    "add": add,
    "-ci": ci_all
}

if __name__ == "__main__":
    main()
