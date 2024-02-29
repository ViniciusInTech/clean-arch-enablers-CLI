import json

from core.entities.ArchFlow import ArchFlow
import subprocess
import sys
import os
import xml.etree.ElementTree as ET


class ArchFlowJavaWeb(ArchFlow):

    def __init__(self):
        super().__init__()
        self.StringManipulator.tag_functions_user = {"artifact_id": self.artifact_id,
                                                     "group_id": self.group_id}

    def create_project(self, group_id, artifact_id, version, package_name, dependencies=None):
        maven_command = [
            "mvn",
            "archetype:generate",  # Corrected the typo here
            "-DgroupId=" + group_id,
            "-DartifactId=" + artifact_id,
            "-Dversion=" + version,
            "-Dpackage=" + package_name,
            "-DarchetypeArtifactId=maven-archetype-quickstart",  # Corrected the prefix here
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
        return {
            "buscar_pom": self.buscar_pom
        }

    def buscar_pom(self):
        poms = self.DirectoryExplorer.list_files("pom.xml")
        core_pom_path = self.find_item_with_key(poms, "Core")
        content = self.DirectoryExplorer.read_file(core_pom_path)
        return self.extrair_valores_pom(content)

    def artifact_id(self, input_string):
        group, artifact = self.buscar_pom()
        return artifact

    def group_id(self, input_string):
        group, artifact = self.buscar_pom()
        return group

    def extrair_valores_pom(self, conteudo_pom):
        try:
            root = ET.fromstring(conteudo_pom)

            group_id = root.find(".//groupId")
            artifact_id = root.find(".//artifactId")

            return (group_id.text if group_id is not None else None,
                    artifact_id.text if artifact_id is not None else None)

        except ET.ParseError:
            self.OutputHandler.information_message("Erro ao analisar o conteúdo XML.")
            return None, None



    @staticmethod
    def find_item_with_key(lista, chave):
        for item in lista:
            if chave in item:
                return item
        return None

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

    def read_json_file(self, path_relative):
        try:
            root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), path_relative))

            with open(root_path, 'r') as file_json:
                content = json.load(file_json)
        except Exception as e:
            self.OutputHandler.alert_message(f"Error reading file {path_relative} error: {e}")
        return content

    def handler_input(self, args):
        def execute_step(steps_function, args_):
            for dic in steps_function:
                for step in dic:
                    args_function = self.find_key_in_dictionaries(dic, step)
                    function = self.find_key_in_dictionaries(dictonary_functions, step)
                    if function is None:
                        function = self.find_key_in_dictionaries(functions_json, step)
                        steps_funcao = self.find_key_in_dictionaries(function, 'steps')
                        args_function_ = self.find_key_in_dictionaries(dic, step)
                        args_mapeados = self.map_args(args_function_, args_[0:], "tem[")
                        execute_step(steps_funcao, args_mapeados)
                        break
                    try:
                        if args_function == "None":
                            function()
                        elif isinstance(args_function, list):
                            args_mapeados = self.map_args(args_function, args_[0:])
                            function(*args_mapeados)
                        else:
                            function(*args_[1:])
                    except TypeError as e:
                        self.OutputHandler.alert_message(f"Error calling the function: {e}")

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
            execute_step(steps_funcao, args)
        else:
            self.OutputHandler.alert_message(f"function '{nome_funcao}' is not valid, try another one or try --help ")



    def map_args(self, list_args, list_replace, parameter="args["):
        args_replace = []
        args_and_tags_replace = []
        for obj in list_args:
            if isinstance(obj, list):
                mapped_list = self.map_args(obj, list_replace, parameter)
                args_replace.append(mapped_list)
            else:
                for i, arg in enumerate(list_replace):
                    obj = obj.replace(f"{parameter}{i}]", arg)
                args_replace.append(obj)
        for tag in args_replace:
            if isinstance(tag, list):
                subs = []
                for sub_ in tag:
                    tag_replace = self.StringManipulator.replace_tags(sub_)
                    subs.append(tag_replace)
                args_and_tags_replace.append(subs)
            else:
                tag_replace = self.StringManipulator.replace_tags(tag)
                args_and_tags_replace.append(tag_replace)
        return args_and_tags_replace

