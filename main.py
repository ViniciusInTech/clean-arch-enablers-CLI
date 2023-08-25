import sys
from authCae import is_valid_args, is_a_java_project
from criateDirAndFiles import createDir, create_use_case_fuc, create_folder_structure
from findDir import find_folder
from utils import split_words, join_words, to_snake_case, to_pascal_case
from variables import ignore_args_first, input_word_position


def main():
    args = sys.argv[ignore_args_first:]
    if is_a_java_project() and is_valid_args(args):
        name_case = split_words(args[input_word_position])
        create_folder_structure(name_case)
        #create_use_case_fuc(name_case, find_folder(to_snake_case(name_case)))
    else:
        print("could not find java project or invalid arguments")


if __name__ == "__main__":
    main()
