from PyQt6 import QtWidgets, uic
from PyQt6.QtCharts import QPieSeries, QChart, QChartView
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QVBoxLayout

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('UI.ui', self)

        # Tạo dữ liệu cho biểu đồ Pie
        self.series = QPieSeries()
        self.series.append("Python", 0)
        self.series.append("C++", 0)
        self.series.append("Java", 0)
        self.series.append("C#", 0)
        self.series.append("PHP", 0)

        # Tạo biểu đồ từ dữ liệu
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Biểu đồ Pie")

        # Tạo QChartView để hiển thị biểu đồ
        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Tạo QVBoxLayout để chứa QChartView
        layout = QVBoxLayout()
        layout.addWidget(self.chartView)

        # Hiển thị biểu đồ trong graphicsView
        self.graphicsView.setLayout(layout)
        self.show()
        self.pushButton.clicked.connect(self.update_chart)

    def update_chart(self):
        # Lấy ra các giá trị từ self.lineEdit, self.lineEdit_2, ..., self.lineEdit_5
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
window = Ui()
app.exec()
