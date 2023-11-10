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
