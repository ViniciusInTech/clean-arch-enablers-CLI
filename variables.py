import os

ignore_the_first_arg = 1

arg_index_of_use_case_name = 2

arg_function_index = 1

limit_args = 2

valid_args = ["new", "function-use-case", "consume-use-case",
              "supplier-use-case", "runnable-use-case", "fuc",
              "cuc", "suc", "ruc"]

java_project_validator_file = "pom.xml"

write_permission = "w"

filter_package_java = "java\\"

filter_java = 1

dir_of_code = os.path.dirname(os.path.abspath(__file__))
dir_of_config = dir_of_code + "\\config\\functions"


structure_root_folder = "use_cases"

name_of_file_structure_dir = "\\dir_structure.txt"

regex_to_replace_template = r"<<(.*?)>>"

file_folder_name = "\\files"
