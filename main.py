import sys
from authCae import is_valid_args, is_a_java_project
from handle_input_defs import handle_input
from variables import ignore_args_first


def main():
    args = sys.argv[ignore_args_first:]
    if is_a_java_project() and is_valid_args(args):
        handle_input(args)
    else:
        print("could not find java project or invalid arguments")


if __name__ == "__main__":
    main()
