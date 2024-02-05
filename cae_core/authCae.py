import os

from cae_core.searchAndRead import list_files_on_folder
from cae_core.variables import valid_args, java_project_validator_file


arg_function_min_args = {
    "new": 2,
    "add": 1,
    "-ci": 0
}


def is_a_java_project():
    path = os.getcwd()

    files = list_files_on_folder(path)
    for file in files:
        if file.endswith(java_project_validator_file):
            return True
    return True


def find_limit(function):
    if function in arg_function_min_args:
        return arg_function_min_args[function]
    return None


def is_valid_args(args):
    if not args or len(args) <= find_limit(args[0]):
        print('Invalid number of args. Options:')
        print(";\n".join(valid_args))
        return False
    if find_limit(args[0]) is None:
        return False
    args = args[:find_limit(args[0])]
    for arg in args:
        if arg not in valid_args:
            print(f"arg: '{arg}' is Invalid")
            print('args valid: ', valid_args)
            return False
    return True
