import os

def filter_dir_and_files(path):
    content = os.listdir(path)
    folders = []
    files = []

    for item in content:
        if os.path.isdir(os.path.join(path,item)):
            folders.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)

    return folders, files

def list_dir_on_folder(path):
    try:
        folders, _ = filter_dir_and_files(path)

        return folders

    except OSError as e:
        print(f"nada encontrado no dir: {e}")
        return []

def list_files_on_folder(path):
    try:
        _, files = filter_dir_and_files(path)

        return files

    except OSError as e:
        print(f"Error ao listar files: {e}")

def is_a_java_project():
    path = os.getcwd()
    pom = "pom.xml"

    files = list_files_on_folder(path)
    for file in files:
        if file.endswith(pom):
            return True
    return False

def find_folder(target_folder):
    path = os.getcwd()
    for root, directories, _ in os.walk(path):
        if target_folder in directories:
            return os.path.join(root, target_folder)
    return None


