from criateDirAndFiles import create_folder_structure
from findDir import structure_dir_function, structure_file_functions
from variables import input_function_position, input_word_position


def function_use_case(args):
    arg = args[input_word_position]
    dir_structure = structure_dir_function(args[1])
    create_folder_structure(arg, dir_structure)
    structure_file_functions(args[1], arg)
    #create_files_structure(arg)


def consume_use_case(args):
    print("consume use case")


function_mapping = {
    "function-use-case": function_use_case,
    "fuc": function_use_case,
    "consume-use-case": consume_use_case,
    "cuc": consume_use_case
}


def handle_input(args):
    function_name = args[input_function_position]
    function = function_mapping.get(function_name)
    if callable(function):
        function(args)
    else:
        print("Function not found!")


