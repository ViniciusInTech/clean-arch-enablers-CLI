import sys

from authCae import is_valid_args, is_a_java_project
from db import *
from criateFilesAndFolders import create_folder_structure, create_file_structure
from template_commands_json import new_file_json, new_function_json
from variables import ignore_the_first_arg, arg_index_of_use_case_name, arg_function_index, function_index


def main():
    args = sys.argv[ignore_the_first_arg:]
    if is_valid_args(args):
        options_functions[args[function_index]](args)
    else:
        print("invalid arguments")


def new(args):
    if is_a_java_project():
        arg = args[arg_index_of_use_case_name]
        arg_function_name = args[arg_function_index]
        dir_structure = get_dir_by_function(arg_function_name)
        create_folder_structure(arg, dir_structure)
        create_file_structure(arg, arg_function_name)
    else:
        print("could not find java project")


def add(args):
    names = []
    names.append(args[1])
    dirs = []
    files = []
    print(f"Você está preste a criar um novo template '{args[1]}'")
    while if_yes("do you want add a new name for this template?"):
        name = input("new name: ")
        names.append(name)
    while if_yes("do you want add a new dir for create in this template?"):
        dir = input("new dir: ")
        dirs.append(dir)
    while if_yes("do you want add a new file for create in this template?"):
        name = input("name of file: ")
        path = input("path relative of file: ")
        content = input("content of file: ")
        files.append(new_file_json(name, path, content))
    template_json = new_function_json(names, dirs, files)
    save_new_function(template_json, names[0])


def if_yes(question):
    while True:
        p = input(f"{question} y/n ")
        if p.lower() == 'y':
            return True
        if p.lower() == 'n':
            return False
        else:
            print("not valid, options: y our n")


options_functions = {
    "new": new,
    "add": add
}

if __name__ == "__main__":
    main()
