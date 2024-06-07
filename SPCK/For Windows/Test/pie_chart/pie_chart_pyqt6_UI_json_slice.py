from PyQt6 import QtWidgets, uic
from PyQt6.QtCharts import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import qdarktheme
import sys
import json

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Test/pie_chart/UI.ui', self)
        # import json
        with open('Test/pie_chart/json.json', 'r') as f:
            data = json.load(f)

        # Tạo dữ liệu cho biểu đồ Pie Chart
        self.series = QPieSeries()
        for item in data:
            self.series.append(item['name'], item['quantity'])
        
        # for slice in self.series.slices():
            # slice.setLabel("{:.2f}%".format(100 * slice.percentage()))

        # Tạo biểu đồ từ dữ liệu
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Pie Chart")
        self.chart.legend().setFont(QFont("Arial", 12))
        self.chart.setTitleFont(QFont("Arial", 15))
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Tạo QChartView để hiển thị biểu đồ
        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Tạo QVBoxLayout để chứa QChartView
        layout = QVBoxLayout()
        layout.addWidget(self.chartView)

        # Hiển thị biểu đồ trong graphicsView
        self.graphicsView.setLayout(layout)
        self.show()
        
        for i in range(len(self.series.slices())):
            slice = QPieSlice()
            slice = self.series.slices()[i]
            slice.setExploded(True)
            slice.setLabelVisible(True)

        # Các phương thức
        self.pushButton.clicked.connect(self.update_chart)

    def update_chart(self):
        values = [
            int(self.lineEdit.text()),
            int(self.lineEdit_2.text()),
            int(self.lineEdit_3.text()),
            int(self.lineEdit_4.text()),
            int(self.lineEdit_5.text())
        ]
        slices = self.series.slices()

        for value, slice in zip(values, slices):
            slice.setValue(value)
        self.chartView.update()

app = QtWidgets.QApplication([])
app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
window = Ui()
app.exec()