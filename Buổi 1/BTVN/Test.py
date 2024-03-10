# PyQt6
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys

class Main(QMainWindow):
    full = ""
    def __init__ (self):
        super().__init__()
        uic.loadUi("Buổi 1\BTVN\calculate.ui", self)
        self.pushButton.clicked.connect(self.one)
        self.pushButton_5.clicked.connect(self.two)
        self.pushButton_4.clicked.connect(self.three)
        self.pushButton_2.clicked.connect(self.four)
        self.pushButton_9.clicked.connect(self.five)
        self.pushButton_10.clicked.connect(self.six)
        self.pushButton_13.clicked.connect(self.seven)
        self.pushButton_12.clicked.connect(self.eight)
        self.pushButton_14.clicked.connect(self.nine)
        self.pushButton_7.clicked.connect(self.zero)
        self.pushButton_6.clicked.connect(self.dot)
        self.pushButton_3.clicked.connect(self.divide)
        self.pushButton_11.clicked.connect(self.multiply)
        self.pushButton_15.clicked.connect(self.minus)
        self.pushButton_16.clicked.connect(self.plus)
        self.pushButton_8.clicked.connect(self.result)
    
    def one(self):
        self.full += "1"
        self.label.setText(self.full)
    
    def two(self):
        self.full += "2"
        self.label.setText(self.full)

    def three(self):
        self.full += "3"
        self.label.setText(self.full)

    def four(self):
        self.full += "4"
        self.label.setText(self.full)
    
    def five(self):
        self.full += "5"
        self.label.setText(self.full)
    
    def six(self):
        self.full += "6"
        self.label.setText(self.full)

    def seven(self):
        self.full += "7"
        self.label.setText(self.full)
    
    def eight(self):
        self.full += "8"
        self.label.setText(self.full)

    def nine(self):
        self.full += "9"
        self.label.setText(self.full)
    
    def zero(self):
        self.full += "0"
        self.label.setText(self.full)

    def dot(self):
        self.full += "."
        self.label.setText(self.full)
    
    def divide(self):
        self.full += "/"
        self.label.setText(self.full)
    
    def multiply(self):
        self.full += "*"
        self.label.setText(self.full)
    
    def minus(self):
        self.full += "-"
        self.label.setText(self.full)

    def plus(self):
        self.full += "+"
        self.label.setText(self.full)
        
    def result(self):
        self.label.setText(str(eval(self.full)))
        self.full = ""

app = QApplication(sys.argv)
main_ui=Main()
main_ui.show()
app.exec()