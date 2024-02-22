import os
from core.entities.exceptions.NotFoundException import NotFoundException
from core.entities.utils.DirectoryExplorerUtil import DirectoryExplorerUtil
from core.entities.output.OutputHandler import OutputHandler


util = DirectoryExplorerUtil
outuput = OutputHandler()


class DirectoryExplorerImplementation:
    @staticmethod
    def list_files(directory, extension=None):
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if extension is None or filename.endswith(extension):
                    files.append(os.path.join(root, filename))
        if len(files) == 0:
            message_error = f"files with name or extension '{extension}' on directory '{directory}' is None" \
                if extension else \
                f"this directory '{directory}' is empty"
            return NotFoundException.not_found_error(message_error)
        return files

    @staticmethod
    def list_folders(directory, folder=None):
        folders = []
        for root, dirs, files in os.walk(directory):
            for d in dirs:
                folder_path = os.path.join(root, d)
                folders.append(folder_path)

        if folder is not None:
            folders = [f for f in folders if os.path.basename(f) == folder]

        if len(folders) == 0:
            message_error = f"folders with name '{folder}' on directory '{directory}' is None" \
                if folder else \
                f"this directory '{directory}' is empty"
            return NotFoundException.not_found_error(message_error)

        return folders

    @staticmethod
    def find_only_file(directory, file):
        files = DirectoryExplorerImplementation.list_files(directory, file)
        qtde_files = len(files) if files is not None else 0
        if qtde_files == 0:
            return NotFoundException.fatal_not_found_error(f"File '{file}' could not be located in the specified "
                                                           f"directory '{directory}'. This file is essential for "
                                                           f"the proper functioning of the application.")
        if qtde_files >= 2:
            return NotFoundException.fatal_not_found_error(f"Multiple files with the name '{file}' have been found "
                                                           f"in the directory '{directory}'. It is highly advisable "
                                                           f"to have only one file with this name to ensure the "
                                                           f"optimal functioning of the application.")
        return files

    @staticmethod
    def find_only_folder(directory, folder):
        folders = DirectoryExplorerImplementation.list_folders(directory, folder)
        qtde_folders = len(folders) if folders is not None else 0
        if qtde_folders == 0:
            return NotFoundException.fatal_not_found_error(f"Folder '{folder}' could not be located in the specified "
                                                           f"directory '{directory}'. This folder is essential for "
                                                           f"the proper functioning of the application.")
        if qtde_folders >= 2:
            return NotFoundException.fatal_not_found_error(f"Multiple folders with the name '{folder}' have been found "
                                                           f"in the directory '{directory}'. It is highly advisable "
                                                           f"to have only one folder with this name to ensure the "
                                                           f"optimal functioning of the application.")
        return folders

    @staticmethod
    def find_files_ignoring_this_folder(directory, file, folder_to_ignore):
        files = DirectoryExplorerImplementation.list_files(directory, file)
        return util.filter_entities_by_name(files, folder_to_ignore)

    @staticmethod
    def find_folders_ignoring_this_folder(directory, folder, folder_to_ignore):
        folders = DirectoryExplorerImplementation.list_folders(directory, folder)
        return util.filter_entities_by_name(folders, folder_to_ignore)

    @staticmethod
    def read_file(file_path, required=False):
        file_path = util.convert_to_string(file_path)
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            if required:
                return NotFoundException.fatal_not_found_error(f"File required not found: {file_path}")
            return NotFoundException.not_found_error(f"File not found: {file_path}")
        except Exception as e:
            return NotFoundException.fatal_not_found_error(f"Error reading file:{file_path} \nerror {str(e)}")

    @staticmethod
    def change_folder(path_folder, path_root):
        try:
            new_path_root = os.path.join(path_root, path_folder)
            os.chdir(new_path_root)
            outuput.information_message(f"Temporarily moved to folder: {new_path_root}")

        except FileNotFoundError:
            NotFoundException.not_found_error(f"folder not found: {path_folder}")
        except PermissionError:
            outuput.alert_message(f"permission denied to access folder: {path_folder}")

    @staticmethod
    def return_root_path(path_root):
        os.chdir(path_root)
        outuput.information_message(f"Returned to the original folder: {path_root}")
