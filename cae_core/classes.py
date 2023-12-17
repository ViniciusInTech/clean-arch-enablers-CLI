import os
class FilesClass:
    def __init__(self, data):
        self.name = data['name']
        self.path = data['path']
        self.content = data['content']

    def GetName(self):
        return self.name

    def GetPath(self):
        return self.path

    def GetContent(self):
        return self.content


def MapToFile(data):
    files_data = data['files']
    files = []
    for file in files_data:
        files.append(FilesClass(file))
    return files

class DependenciesClass:
    def __init__(self, groupId, artifactId, version):
        self.groupId = groupId
        self.artifactId = artifactId
        self.version = version

    def getGroupId(self):
        return self.groupId

    def getArtifactId(self):
        return self.artifactId

    def getVersion(self):
        return self.version


class ProjectClass:
    def __init__(self, name, path, dependencies):
        self.name = name
        self.path = path
        self.dependencies = dependencies  # Armazena as dependências como uma lista de objetos DependenciesClass

    def GetName(self):
        return self.name

    def GetPath(self):
        return self.path

    def GetDependencies(self):
        return self.dependencies


class FunctionClass:
    def __init__(self, data):
        self.name = data['name']
        self.dir = data['dir']
        self.files = MapToFile(data)

    def GetName(self):
        return self.name

    def GetDir(self):
        return self.dir

    def GetFiles(self):
        return self.files
