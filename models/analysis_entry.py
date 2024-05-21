# analysis_entry.py
# Analysis entry представляет собой результат выбора и предварительной настройки одного слота
# в add_project.html
# Он имеет следующую структуру:
# 1. Основной файл данных (открытый и обработанный csv-файл с отфильтрованными данными) 
# 2. Дополнительный маркированный файл (каждая запись в нем отнесена к одному из классов)
# 3. Дополнительный файл для таблицы Overview плюс ее футер
# 4. Дополнительный файл для таблицы All
# 5. Дополнительный файл для таблицы New
# 6. Дополнительный файл для таблицы Link Types

class Analysis_Entry:
    def __init__(self, path, filename):
        self.entry_path = path
        self.filename = filename
        self.basefileready = self.makeBaseFile()
        self.markfileready = self.makeMarkFile()
        self.overfileready = self.makeOverFile()
        self.allfileready = self.makeAllFile()
        self.newfileready = self.makeNewFile()
        self.linkfileready = self.makeLinkFile()

    getEntryPath = lambda self: self.entry_path

    def makeBaseFile(self):
        return True

    def makeMarkFile(self):
        return True

    def makeOverFile(self):
        return True

    def makeAllFile(self):
        return True

    def makeNewFile(self):
        return True

    def makeLinkFile(self):
        return True


