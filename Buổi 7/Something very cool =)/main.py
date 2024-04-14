from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Buổi 7\\Something very cool =)\\breh.ui", self)
        a = ["item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7", "item 8", "item 9", "item 10"]
        self.listWidget_2.addItems(a)
        self.pushButton_11.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.remove)
        print(self.listWidget_2.count())
        
    def add(self):
        self.listWidget_2.addItem(self.lineEdit.text())
        self.lineEdit.clear()
    
    def remove(self):
        self.listWidget_2.takeItem(self.listWidget_2.currentRow())


app = QApplication(sys.argv)
main_ui = Main()
main_ui.show()
app.exec()