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


class ProjectClass:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def GetName(self):
        return self.name

    def GetPath(self):
        return self.path


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
