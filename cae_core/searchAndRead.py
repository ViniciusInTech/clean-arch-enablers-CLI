import os


def filter_dir_and_files(path):
    content = os.listdir(path)
    folders = []
    files = []

    for item in content:
        
        if os.path.isdir(os.path.join(path, item)):
            folders.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)

    return folders, files


def list_dir_on_folder(path):
    try:
        folders, _ = filter_dir_and_files(path)

        return folders

    except OSError as e:
        print(f"There was nothing in dir: {e}")
        return []


def list_files_on_folder(path):
    try:
        _, files = filter_dir_and_files(path)
        return files

    except OSError as e:
        print(f"Error while listing files: {e}")


def read_file_txt(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"The file {path} was not found.")
        return []


def find_folder(target_folder):
    for root, directories, _ in os.walk('.'):
        if target_folder in directories:
            relative_path = os.path.relpath(os.path.join(root, target_folder))
            return relative_path
    return None

def find_folder_absolute(target_folder):
    for root, directories, _ in os.walk('.'):
        if target_folder in directories:
            absolute_path = os.path.abspath(os.path.join(root, target_folder))
            return absolute_path
    return None
