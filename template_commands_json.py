def new_function_json(names, dirs, files):
    estrutura_json = {
        "name": names,
        "dir": dirs,
        "files": files
    }
    return estrutura_json


def new_file_json(name, path, content):
    return {
        "name": name,
        "path": path,
        "content": content
    }


"""names = ["function use case", "fuc", "functionUseCase"]
dirs = ["factories","factories\\dependency_wrapper","implementations","implementations\\ports","io","io\\inputs","io\\outputs"]
files = [{
          "name":"teste.java",
          "path":"\\<<case_name_snake_case>>\\",
          "content":"arquivo"
          },
         {"name":"teste1.java",
          "path":"\\case_name",
          "content":"teste"
         }
         ]

print(new_function_json(names, dirs, files))
"""

