import os
import sys

from cae_core.authCae import is_valid_args, is_a_java_project
from cae_core.createProject import create_dir_structure_pk, create_maven_project, create_project_pk
from cae_core.searchAndRead import list_dir_on_folder, find_folder, find_folder_absolute
from cae_core.utils import open_in_nano, filtrar_itens
from cae_plugins.db import *
from cae_core.criateFilesAndFolders import create_folder_structure, create_file_structure, mudar_diretorio
from cae_plugins.template_commands_json import new_file_json, new_function_json
from cae_core.variables import ignore_the_first_arg, arg_index_of_use_case_name, arg_function_index, function_index


def main():
    args = sys.argv[ignore_the_first_arg:]
    if is_valid_args(args):
        options_functions[args[function_index]](args)
    else:
        print("invalid arguments")


def new(args):
    function = args[arg_function_index]
    if is_a_java_project() and function == "fuc":
        arg = args[arg_index_of_use_case_name]
        arg_function_name = args[arg_function_index]
        dir_root = os.getcwd()
        itens = filtrar_itens(list_dir_on_folder(os.getcwd()), ['Adaptadores', 'Core', "Montadores"])

        for i in itens:
            mudar_diretorio(find_folder_absolute(i))
            dir_structure = get_dir_by_function("fuc_"+i)
            create_folder_structure(arg, dir_structure)
            create_file_structure(arg, "fuc_"+i)
            mudar_diretorio(dir_root)
            print("fuc_"+i)
    if args[arg_function_index] == "project":
        arg_list = []
        arg = args[arg_index_of_use_case_name]
        arg_list.append(arg)
        group_id = args[arg_index_of_use_case_name+1]
        create_dir_structure_pk(arg)
        create_file_structure(arg, args[1])
        create_project_pk(group_id, arg_list)
    else:
        pass


def add(args):
    names = [args[1]]
    print(f"You are about to create a new template '{args[1]}'")
    print(f"press only ENTER to exit")
    names = name_add(names)
    dirs = dir_add()
    files = file_add()
    template_json = new_function_json(names, dirs, files)
    save_new_function(template_json, names[0])


def name_add(names):
    print(" ")
    print("ID name for this templates")
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
        path = input("path relative of file: ")
        input("Press any to open editor for content template")
        content = open_in_nano()
        files.append(new_file_json(name, path, content))
    return files


options_functions = {
    "new": new,
    "add": add
}

if __name__ == "__main__":
    main()
