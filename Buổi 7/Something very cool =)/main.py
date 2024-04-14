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
        self.show()


app = QApplication(sys.argv)
main_ui = Main()
main_ui.show()
app.exec()