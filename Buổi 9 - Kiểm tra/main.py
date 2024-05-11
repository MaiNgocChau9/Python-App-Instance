from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys

import json

class Homework:
    def __init__(self, name, priority, completed):
        self.name = name
        self.priority = priority
        self.completed = completed
    
class HomeworkList:
    def __init__(self):
        self.items = []
        self.un_finished = []
    
    def add(self, item):
        self.items.append(item)
    
    def remove(self, name):
        for i in self.items:
            if i.name == name:
                self.items.remove(i)

homeworklist = HomeworkList()

#! Tạo danh sách các bài tập
data = open("data.json", encoding="utf-8")
data = data.read()
data = json.loads(data)

for i in data:
    homeworklist.add(Homework(i["name"], i["priority"], i["completed"]))

#! Main program
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        #! Set font
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        for i in homeworklist.items:
            self.listWidget_2.addItem(i.name)

        self.pushButton_3.setFont(font)
        self.pushButton_11.setFont(font)

        self.pushButton_11.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.export)

    def export(self):
        export_ui.show()
    
    def add(self):
        add_ui.show()

    def reload_ui(self):
        self.listWidget_2.clear()
        for i in homeworklist.items:
            self.listWidget_2.addItem(i.name)

class Export(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("export.ui", self)
        
        #! Set font
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_11.setFont(font)
        for i in homeworklist.items:
            self.listWidget_2.addItem(i.name)
        self.pushButton_11.clicked.connect(self.export_json)
    
    def export_json(self):
        with open("new_data.json", "w", encoding="utf-8") as f:
            data = []
            for i in range(len(homeworklist.items)):
                item = {
                    "name": homeworklist.items[i].name,
                    "priority": homeworklist.items[i].priority,
                    "completed": homeworklist.items[i].completed,
                }
                data.append(item)
            json.dump(data, f, indent=4, ensure_ascii=False)


class Add(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("add.ui", self)
        
        #! Set font
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.add)

    def add(self):
        name = self.lineEdit.text()
        priority = self.lineEdit_2.text()
        completed = self.lineEdit_3.text()
        homeworklist.add(Homework(name, priority, completed))
        with open("data.json", "w", encoding="utf-8") as f:
            data = []
            for i in range(len(homeworklist.items)):
                item = {
                    "name": homeworklist.items[i].name,
                    "priority": homeworklist.items[i].priority,
                    "completed": homeworklist.items[i].completed,
                }
                data.append(item)
            json.dump(data, f, indent=4, ensure_ascii=False)
        self.close()
        main_ui.reload_ui()

app = QApplication(sys.argv)

main_ui = Main()
export_ui = Export()
add_ui = Add()

main_ui.show()
app.exec()