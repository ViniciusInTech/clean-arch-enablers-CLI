from abc import ABC, abstractmethod
from core.entities.DirectoryCreator import DirectoryCreator
from core.entities.DirectoryExplorer import DirectoryExplorer
from core.entities.StringManipulator import StringManipulator
from core.entities.output.OutputHandler import OutputHandler
import ascii
import os


class ArchFlow(ABC):
    def __init__(self):
        self.DirectoryCreator = DirectoryCreator()
        self.DirectoryExplorer = DirectoryExplorer()
        self.StringManipulator = StringManipulator()
        self.OutputHandler = OutputHandler()
        self.diretorio_original = os.getcwd()

    @abstractmethod
    def create_project(self, *args):
        pass

    @abstractmethod
    def functions_flow(self):
        pass

    @staticmethod
    def version():
        url = 'https://i.pinimg.com/474x/bf/d0/09/bfd00921d5869955086cc761c1d6100a.jpg'
        output = ascii.loadFromUrl(url)
        print(output)
        print("⚡️ Cae Version 1.1 ⚡️")
        print("⚡️ ArchFlow Version 1.0 ⚡️")
        print("Pikachu is evolving... slowly. But hey, we still love him! 🤣⚡️")

    def create_file_based_in_template(self, file_destination, file_name, template_file_name, args=None):
        file_destination = file_destination
        content = self.DirectoryExplorer.read_file_template(template_file_name)
        if args:
            content = self.StringManipulator.replace_args(content, args)
        content = self.StringManipulator.replace_tags(content)
        self.DirectoryCreator.create_file(file_destination, file_name, content)

    def dictionary_of_standard_functions(self):
        dictionary_directory_creator = self.DirectoryCreator.dictionary_of_standard_functions()
        dictionary_directory_explorer = self.DirectoryExplorer.dictionary_of_standard_functions()
        dictionary_string_manipulator = self.StringManipulator.dictionary_of_standard_functions()
        dictionary_output_handler = self.OutputHandler.dictionary_of_standard_functions()
        functions_flow = self.functions_flow()
        return {'create_project': self.create_project,
                'functions_flow': functions_flow,
                'directory_creator': dictionary_directory_creator,
                'directory_explorer': dictionary_directory_explorer,
                'string_manipulator': dictionary_string_manipulator,
                'output_handler': dictionary_output_handler,
                'create_file_based_in_template': self.create_file_based_in_template,
                '--version': self.version,
                '-v': self.version,
                }

