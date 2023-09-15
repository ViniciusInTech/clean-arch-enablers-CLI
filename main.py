import sys

from authCae import is_valid_args, is_a_java_project
from criateFilesAndFolders import create_dir_structure, create_folder_structure, create_file_structure
from variables import ignore_the_first_arg, arg_index_of_use_case_name, arg_function_index


def main():
    args = sys.argv[ignore_the_first_arg:]
    if is_a_java_project() and is_valid_args(args):
        arg = args[arg_index_of_use_case_name]
        arg_function_name = args[arg_function_index]
        dir_structure = create_dir_structure(arg_function_name)
        create_folder_structure(arg, dir_structure)
        create_file_structure(arg_function_name, arg)
    else:
        print("could not find java project or invalid arguments")


if __name__ == "__main__":
    main()
