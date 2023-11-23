import os
import subprocess

from cae_core.classes import ProjectClass
from cae_core.criateFilesAndFolders import create_dir, replace_tag
from cae_core.utils import split_words
from cae_core.variables import barra_system
from cae_plugins.db import get_function_by_name, get_project


def create_dir_pk(dir_structure):
    path = os.getcwd()
    for dir in dir_structure:
        create_dir(path + barra_system + dir)

def create_project_pk(group_id, artifact_id):
    projects = project_name_and_path(get_project(), artifact_id)
    path = os.getcwd()+barra_system
    for project in projects:
        directory = path + project.GetPath()
        create_maven_project(group_id, project.GetName(), directory)


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
            projects_obj.append(ProjectClass(name_tag, path_tag))
        else:
            projects_obj.append(ProjectClass(p['name'], p['path']))
    return projects_obj


def create_maven_project(group_id, artifact_id, directory):
    try:
        os.makedirs(directory, exist_ok=True)  # Criar o diretório se não existir
        os.chdir(directory)  # Mudar para o diretório do projeto
        command_maven = f"mvn archetype:generate -DgroupId={group_id} -DartifactId={artifact_id} -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false"
        subprocess.run(command_maven, shell=True, check=True)
        print(f"Projeto Maven {artifact_id} criado com sucesso no diretório {directory}!")
    except subprocess.CalledProcessError as erro:
        print(f"Erro ao criar o projeto Maven: {erro}")


