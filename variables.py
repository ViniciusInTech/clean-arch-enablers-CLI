import os

dir_of_code = os.path.dirname(os.path.abspath(__file__))

dir_of_config = dir_of_code + "\\config\\functions"

ignore_args_first = 1

input_word_position = 2

input_function_position = 1

limit_args = 2

valid_args = ["new", "function-use-case", "consume-use-case",
              "supplier-use-case", "runnable-use-case", "fuc",
              "cuc", "suc", "ruc"]

java_project_validator_file = "pom.xml"

write_permission = "w"

filter_package_java = "java\\"

filter_java = 1


dir_to_be_created = []
"""["factories",
                     "factories\\dependency_wrapper",
                     "implementations",
                     "implementations\\ports",
                     "io",
                     "io\\inputs",
                     "io\\outputs"]"""

file_to_be_created = ["case_nameUseCase.java",
                      "factories\\case_nameUseCaseFactory.java",
                      "factories\\dependency_wrapper\\case_nameUseCaseDependencyWrapper.java",
                      "implementations\\case_nameUseCaseImplementation.java",
                      "io\\inputs\\case_nameUseCaseInput.java", "io\\outputs\\case_nameUseCaseOutput.java"]


