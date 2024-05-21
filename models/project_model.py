import datetime
from models.filer import Filer

class Project_model:
    def __init__(self, path, name, owner, date=datetime.date.today()):
        self.project_path = path
        self.project_name = name
        self.project_owner = owner
        self.project_date = str(date)
    
    getPath = lambda self: self.project_path

    getName = lambda self: self.project_name

    getOwner = lambda self: self.project_owner

    getDate = lambda self: self.project_date

    def deleteProject(self):
        try:
            Filer(self.project_path).removeDir()
        except Exception as ex:
            raise Exception(f'Cannot delete project, {ex}')

    def createProject(self):
        j = 1
        own_path = self.project_path
        while True:
            if Filer(own_path).isExists():
                own_path = self.project_path + str(j)
                j += 1
            else:
                self.project_path = own_path
                r1 = {}
                r1['project_name'] = self.project_name
                r1['project_path'] = self.project_path
                r1['project_owner'] = self.project_owner
                r1['project_date'] = self.project_date
                try:
                    Filer(self.project_path).makeDir()
                except Exception as ex:
                    raise Exception('Cannote make directory')
                Filer(self.project_path + '/model.json').saveDictAsJson(r1)
                break
        return True

    # Регистрация проекта
    def registerProject(self, filename):
        projects = Filer(filename).loadDictFromJson()
        r1 = {}
        r1['project_name'] = self.project_name
        r1['project_path'] = self.project_path
        r1['project_owner'] = self.project_owner
        r1['project_date'] = self.project_date
        try:
            projects.append(r1)
        except Exception as ex:
            raise(ex)
        Filer(filename).saveDictAsJson(projects)

    # Вывод проекта из списка проектов
    def deregisterProject(self, filename):
        projects = Filer(filename).loadDictFromJson()
        res = []
        for project in projects:
            if self.project_path != project['project_path']:
                res.append(project)
        Filer(filename).saveDictAsJson(res)


def createProjectFromDir(dirname):
    r1 = Filer(dirname + '/' + 'model.json').loadDictFromJson()
    return Project_model(r1['project_path'], r1['project_name'], r1['project_owner'], r1['project_date'])
