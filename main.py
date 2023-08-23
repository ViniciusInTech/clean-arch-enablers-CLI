import sys
from authCae import is_valid_args, is_a_java_project
from utils import split_words
from variables import ignore_args_first, input_word_position


def main():
    args = sys.argv[ignore_args_first:]
    if is_a_java_project() and is_valid_args(args):
        print(split_words(args[input_word_position]))
    else:
        print("could not find java project or invalid arguments")

if __name__ == "__main__":
    main()
