from models.project_model import Project_model, createProjectFromDir
import time


"""project1 = Project_model('projects/divenport', 'divenport', 'argile@mail.com')
if project1.createProject():
    print('Project created!')

project2 = Project_model('projects/davenport', 'davenport', 'argile@mail.com')
if project2.createProject():
    print('Project created!')
    time.sleep(20)

project2.registerProject('lists/projects.json')

project2.deregisterProject('lists/projects.json')
project2.deleteProject()
print('Project deleted!')
"""
project3 = createProjectFromDir('projects/divenport')
print(project3.getPath(), project3.getName(), project3.getOwner(), project3.getDate())
project3.deleteProject()
