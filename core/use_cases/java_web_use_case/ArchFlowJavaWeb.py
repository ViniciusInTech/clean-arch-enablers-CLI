import json

from core.entities.ArchFlow import ArchFlow
import subprocess
import sys
import os


class ArchFlowJavaWeb(ArchFlow):

    def create_project(self, group_id, artifact_id, version, package_name, dependencies=None):
        maven_command = [
            "mvn",
            "selfetype:generate",
            "-DgroupId=" + group_id,
            "-DartifactId=" + artifact_id,
            "-Dversion=" + version,
            "-Dpackage=" + package_name,
            "-DselfetypeArtifactId=maven-selfetype-quickstart",
            "-DinteractiveMode=false"
        ]
        try:
            self.OutputHandler.information_message("starting to create a java project using maven")
            process = subprocess.Popen(" ".join(maven_command), shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, text=True)

            for line in process.stdout:
                print(line, end='')

            process.wait()
            if process.returncode == 0:
                self.OutputHandler.success_message(f"Maven project '{artifact_id}' created successfully.")
            else:
                self.OutputHandler.alert_message(f"Error creating Maven project '{artifact_id}'. "
                                                 f"Return code: {process.returncode}")

        except Exception as e:
            self.OutputHandler.alert_message(f"Error executing Maven command: {e}")

    def functions_flow(self):
        pass

    def find_key_in_dictionaries(self, dictionaries, key):
        if key in dictionaries:
            return dictionaries.get(key)
        else:
            for key_ in dictionaries.keys():
                if isinstance(dictionaries.get(key_), dict):
                    dictionary = dictionaries.get(key_)
                    if dictionary is not None:
                        function = self.find_key_in_dictionaries(dictionary, key)
                        if function is not None:
                            return function
        return None
    
    @staticmethod
    def handle_args():
        args_input = sys.argv
        return args_input[1:]
    
    @staticmethod
    def read_json_file(path_relative):
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), path_relative))
        
        with open(root_path, 'r') as file_json:
            content = json.load(file_json)
        return content

    def handler_input(self, args):
        if len(args) == 0:
            self.OutputHandler.success_message("Whoopsie-daisy! It seems like you forgot to provide a function. "
                                               "How about trying --help for some magic commands?")
            return None

        functions_json = self.read_json_file("db.json")
        nome_funcao = args[0]

        func = self.find_key_in_dictionaries(functions_json, nome_funcao)
        if func is not None:
            steps_funcao = self.find_key_in_dictionaries(func, 'steps')
            dictonary_functions = self.dictionary_of_standard_functions()
            for dic in steps_funcao:
                for step in dic:
                    args_function = self.find_key_in_dictionaries(dic, step)
                    function = self.find_key_in_dictionaries(dictonary_functions, step)
                    try:
                        if args_function == "None":
                            function()
                        elif isinstance(args_function, list):
                            args_mapeados = self.map_args(args_function, args[1:])
                            function(*args_mapeados)
                        else:
                            function(*args[1:])
                    except TypeError as e:
                        self.OutputHandler.alert_message(f"Error calling the function: {e}")
        else:
            self.OutputHandler.alert_message(f"function '{nome_funcao}' is not valid, try another one or try --help ")

    def map_args(self, list_args, list_replace):
        args_replace = []
        args_and_tags_replace = []
        for obj in list_args:
            for i, arg in enumerate(list_replace):
                obj = obj.replace(f"args[{i}]", arg)
            args_replace.append(obj)
        for tag in args_replace:
            tag_replace = self.StringManipulator.replace_tags(tag)
            args_and_tags_replace.append(tag_replace)
        return args_and_tags_replace
