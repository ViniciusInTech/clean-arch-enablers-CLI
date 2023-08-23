import os
from findDir import list_files_on_folder
from variables import limit_args, valid_args, java_project_validator_file


def is_a_java_project():
    path = os.getcwd()

    files = list_files_on_folder(path)
    for file in files:
        if file.endswith(java_project_validator_file):
            return True
    return False


def is_valid_args(args):
    if not args or len(args) <= limit_args:
        print('Number of args invalid. options:')
        print(";\n".join(valid_args))
        return False
    args = args[:limit_args]
    for arg in args:
        if arg not in valid_args:
            print('arg: ', arg, 'Invalid')
            print('args valid: ', valid_args)
            return False
    return True
