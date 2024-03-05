from core.entities.ArchFlow import ArchFlow
from core.entities.utils.Filter import Filter
import subprocess
import sys
import os
import xml.etree.ElementTree as ET


filter = Filter()


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
        core_pom_path = filter.find_one_obj_by_key(poms, "Core")
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
    def handle_args():
        args_input = sys.argv
        return args_input[1:]

    def handler_input(self, args):
        def execute_step(steps_function, args_):
            for dic in steps_function:
                for step in dic:
                    args_function = filter.find_key_in_dictionaries(dic, step)
                    function = filter.find_key_in_dictionaries(dictonary_functions, step)
                    if function is None:
                        function = filter.find_key_in_dictionaries(functions_json, step)
                        steps_funcao = filter.find_key_in_dictionaries(function, 'steps')
                        args_function_ = filter.find_key_in_dictionaries(dic, step)
                        args_mapeados = filter.map_args(args_function_, args_[0:], "tem[")
                        execute_step(steps_funcao, args_mapeados)
                        break
                    try:
                        if args_function == "None":
                            function()
                        elif isinstance(args_function, list):
                            args_mapeados = filter.map_args(args_function, args_[0:])
                            function(*args_mapeados)
                        else:
                            function(*args_[1:])
                    except TypeError as e:
                        self.OutputHandler.alert_message(f"Error calling the function: {e}")

        if len(args) == 0:
            self.OutputHandler.success_message("Whoopsie-daisy! It seems like you forgot to provide a function. "
                                               "How about trying --help for some magic commands?")
            return None
        root_path_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "db.json"))
        functions_json = self.DirectoryExplorer.read_json_file(root_path_json)
        nome_funcao = args[0]

        func = filter.find_key_in_dictionaries(functions_json, nome_funcao)
        if func is not None:
            steps_funcao = filter.find_key_in_dictionaries(func, 'steps')
            dictonary_functions = self.dictionary_of_standard_functions()
            execute_step(steps_funcao, args)
        else:
            self.OutputHandler.alert_message(f"function '{nome_funcao}' is not valid, try another one or try --help ")
