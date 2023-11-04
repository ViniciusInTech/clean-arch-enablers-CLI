import json
import os
from classes import *

db_path = "db.json"


def load_json(file_path, modo='r'):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(root_dir, file_path)
    try:
        with open(full_path, modo) as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in the '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


def find_key(dados, key):
    try:
        return dados[key]
    except KeyError:
        print(f"don't find key '{key}'")
        return None


def get_all_functions():
    dados = load_json(db_path)["functions"]
    try:
        functions = []
        for function in dados:
            functions.append(FunctionClass(dados[function]))
        return functions

    except Exception:
        print(f"Error in get all functions")
        return None


def get_all_functions_name():
    dados = get_all_functions()
    functions = []
    for function in dados:
        functions.append(function.GetName())
    return functions


def get_by_function(function):
    dados = load_json(db_path)["functions"]
    return FunctionClass(find_key(dados, function))


def get_dir_by_function(function):
    return get_by_function(function).GetDir()


def get_function_by_name(name_function):
    functions = get_all_functions()
    try:
        for function in functions:
            names = function.GetName()
            for name in names:
                if name == name_function:
                    return function
    except Exception:
        print(f"Function '{name_function}' don´t found")
        return None


def get_all_commands():
    dados = load_json(db_path)
    return find_key(dados, "commands")


def map_list(input_list):
    combined_data = []
    for item in input_list:
        if isinstance(item, list):
            combined_data.extend(item)
        else:
            combined_data.append(item)
    return combined_data


def save_json(file_path, data, modo='w'):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(root_dir, file_path)
    try:
        with open(full_path, modo) as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving JSON to '{file_path}': {e}")


def save_new_function(data,name):
    dados = load_json(db_path)
    dados['functions'][name] = data
    save_json(db_path, dados)
    print("New template save sucess!!!")

"""dados = load_json(db_path)
dados['functions']["nova funcao"] = "NovoTeste"
save_json(db_path, dados)"""
#print(load_json(db_path))