from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100,100, 600,600)
 
        self.show()
        self.create_piechart()

    def create_piechart(self):
        series = QtChart.QPieSeries()
        series.append("Python", 80)
        series.append("C++", 70)
        series.append("Java", 50)
        series.append("C#", 40)
        series.append("PHP", 30)
        series.setLabelsVisible(True)
        series.setLabelsPosition(QtChart.QPieSlice.LabelOutside)
        # for slice in series.slices():
        #     slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
 
        chart = QChart()
        chart.legend()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        
        self.setCentralWidget(chartview)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())