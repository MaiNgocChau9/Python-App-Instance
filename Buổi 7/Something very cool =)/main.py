from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys

import json

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("breh.ui", self)

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.pushButton_11.setFont(font)
        self.pushButton.setFont(font)

        self.pushButton_11.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.remove)
        self.pushButton_2.clicked.connect(self.search)

        self.load()

    
    def search(self):
        matched_items = self.listWidget_2.findItems(self.lineEdit.text(), Qt.MatchFlag.MatchContains)
        for i in range(self.listWidget_2.count()):
            it = self.listWidget_2.item(i)
            it.setHidden(it not in matched_items)
    
    def load(self):
        with open('json.json', 'r') as f:
            self.data = json.load(f)

        for i in self.data: self.listWidget_2.addItems([i['name']])
        
    def add(self):
        add_ui.show()
    
    def remove(self):
        with open('json.json', 'r') as f:
            self.data = json.load(f)
        self.data.pop(self.listWidget_2.currentRow())
        with open('json.json', 'w') as f:
            json.dump(self.data, f, indent=4)
        self.load()
    
class Add(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("add.ui", self)
    
        self.pushButton.clicked.connect(self.add)
    
    def add(self):
        with open('json.json', 'r') as f:
            self.data = json.load(f)
        self.data += [{"name": self.lineEdit.text()}]
        with open('json.json', 'w') as f:
            json.dump(self.data, f, indent=4)
        self.close()
        main_ui.load()


app = QApplication(sys.argv)
main_ui = Main()
add_ui = Add()
main_ui.show()
app.exec()