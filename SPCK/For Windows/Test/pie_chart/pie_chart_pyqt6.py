import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCharts import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100,100, 600,600)
        self.show()
        self.create_piechart()
 
    def create_piechart(self):
        series = QPieSeries()
        series.append("Python", 80)
        series.append("C++", 70)
        series.append("Java", 50)
        series.append("C#", 40)
        series.append("PHP", 30)
        # for slice in series.slices():
        #     slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
 
        #adding slice
        for i in range(0, 5):
            slice = QPieSlice()
            slice = series.slices()[i]
            # slice.setExploded(True)
            slice.setLabelVisible(True)
 
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Pie Chart Example")
        chart.legend().setFont(QFont("Arial", 12))
        chart.setTitleFont(QFont("Arial", 15))
        chart.legend().setVisible(True)
        chartview = QChartView(chart)
        self.setCentralWidget(chartview)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())