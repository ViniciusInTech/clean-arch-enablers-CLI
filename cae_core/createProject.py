import os
import subprocess
import glob
import xml.dom.minidom
from cae_core.classes import ProjectClass, DependenciesClass
from cae_core.criateFilesAndFolders import create_dir, replace_tag
from cae_core.utils import split_words
from cae_core.variables import barra_system
from cae_plugins.db import get_function_by_name, get_project
import xml.etree.ElementTree as ET


def create_dir_pk(dir_structure):
    path = os.getcwd()
    for dir in dir_structure:
        create_dir(path + barra_system + dir)

def create_project_pk(group_id, artifact_id):
    projects = project_name_and_path(get_project(), artifact_id)
    path = os.getcwd()+barra_system
    for project in projects:
        directory = path + project.GetPath()
        create_maven_project(group_id, project.GetName(), directory, project.GetDependencies())


def create_dir_structure_pk(name, name_project="project"):
    function = get_function_by_name(name_project)
    dirs = function.GetDir()
    name_dir = split_words(name)
    dirs_tag = []
    for dir in dirs:
        dirs_tag.append(replace_tag(dir, name_dir))
    create_dir_pk(dirs_tag)

def project_name_and_path(projects_list, name=None):
    projects_obj = []
    for p in projects_list:
        if name is not None:
            name_tag = replace_tag(p['name'], name)
            path_tag = replace_tag(p['path'], name)
        else:
            name_tag = p['name']
            path_tag = p['path']

        dependencies = [
            DependenciesClass(dep['groupId'], dep['artifactId'], dep['version'])
            for dep in p.get('dependencies', [])
        ]

        projects_obj.append(ProjectClass(name_tag, path_tag, dependencies))

    return projects_obj
"""def project_name_and_path(projects_list, name=None):
    projects_obj = []
    for p in projects_list:
        if name is not None:
            name_tag = replace_tag(p['name'], name)
            path_tag = replace_tag(p['path'], name)
            projects_obj.append(ProjectClass(name_tag, path_tag,"teste"))
        else:
            projects_obj.append(ProjectClass(p['name'], p['path'], "testse"))
    return projects_obj"""


def find_pom_file(directory):
    pom_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'pom.xml':
                pom_files.append(os.path.join(root, file))
    return pom_files


def remove_namespace(directory):
    pom_files = find_pom_file(directory)

    if not pom_files:
        print("Arquivo 'pom.xml' não encontrado no diretório ou subdiretórios.")
        return

    for pom_path in pom_files:
        tree = ET.parse(pom_path)
        root = tree.getroot()
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
        tree.write(pom_path, encoding='utf-8', xml_declaration=True)


def format_xml(directory):
    pom_files = find_pom_file(directory)

    if not pom_files:
        print("Arquivo 'pom.xml' não encontrado no diretório ou subdiretórios.")
        return

    for pom_path in pom_files:
        with open(pom_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()
            dom = xml.dom.minidom.parseString(xml_content)

        # Reescrever o conteúdo formatado para o arquivo
        with open(pom_path, 'w', encoding='utf-8') as file:
            file.write(dom.toprettyxml(indent='    '))

def remove_blank_lines(directory):
    pom_files = find_pom_file(directory)

    if not pom_files:
        print("Arquivo 'pom.xml' não encontrado no diretório ou subdiretórios.")
        return

    for pom_path in pom_files:
        with open(pom_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()
            dom = xml.dom.minidom.parseString(xml_content)

        # Remover sequências de duas linhas em branco
        lines = dom.toprettyxml(indent='    ').splitlines()
        filtered_lines = [lines[0]]  # Adiciona a primeira linha

        for i in range(1, len(lines)):
            if lines[i].strip() or lines[i - 1].strip():
                filtered_lines.append(lines[i])

        formatted_xml = '\n'.join(filtered_lines)

        # Reescrever o conteúdo sem as sequências de duas linhas em branco
        with open(pom_path, 'w', encoding='utf-8') as file:
            file.write(formatted_xml)

def add_dependency_to_pom(group_id, artifact_id, version, directory):
    pom_files = find_pom_file(directory)

    if not pom_files:
        print("Arquivo 'pom.xml' não encontrado no diretório ou subdiretórios.")
        return

    for pom_path in pom_files:
        try:
            tree = ET.parse(pom_path)
            root = tree.getroot()

            # Encontrar ou criar a seção de dependências no XML
            dependencies = root.find('.//{http://maven.apache.org/POM/4.0.0}dependencies')
            if dependencies is None:
                dependencies = ET.SubElement(root, '{http://maven.apache.org/POM/4.0.0}dependencies')

            # Criar um novo elemento para a dependência
            dependency = ET.Element('{http://maven.apache.org/POM/4.0.0}dependency')
            ET.SubElement(dependency, '{http://maven.apache.org/POM/4.0.0}groupId').text = group_id
            ET.SubElement(dependency, '{http://maven.apache.org/POM/4.0.0}artifactId').text = artifact_id
            ET.SubElement(dependency, '{http://maven.apache.org/POM/4.0.0}version').text = version

            # Adicionar a nova dependência na seção de dependências
            dependencies.append(dependency)

            # Salvar as alterações de volta no arquivo pom.xml
            tree.write(pom_path, xml_declaration=True, encoding='UTF-8')
            print(f"Dependência {artifact_id} adicionada com sucesso ao arquivo 'pom.xml' em {pom_path}!")
            break  # Adicionou em um arquivo, então para o loop
        except Exception as e:
            print(f"Erro ao adicionar a dependência: {e}")

def create_maven_project(group_id, artifact_id, directory, dependency=None):
    try:
        os.makedirs(directory, exist_ok=True)  # Criar o diretório se não existir
        os.chdir(directory)  # Mudar para o diretório do projeto

        command_maven = f"mvn archetype:generate -DgroupId={group_id} -DartifactId={artifact_id} -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false"
        subprocess.run(command_maven, shell=True, check=True)
        print(f"Projeto Maven {artifact_id} criado com sucesso no diretório {directory}!")
        if dependency:
            for d in dependency:
                arti = split_words(artifact_id)[0]
                add_dependency_to_pom(replace_tag(d.getGroupId(),group_id), replace_tag(d.getArtifactId(), arti), d.getVersion(), directory)
            remove_namespace(directory)
            format_xml(directory)
            remove_blank_lines(directory)
    except subprocess.CalledProcessError as erro:
        print(f"Erro ao criar o projeto Maven:")


