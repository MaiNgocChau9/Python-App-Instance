from PyQt6 import QtWidgets, uic
from PyQt6.QtCharts import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import json

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('UI.ui', self)
        
        # import json
        with open('json.json', 'r') as f:
            data = json.load(f)

        # Tạo dữ liệu cho biểu đồ Pie Chart
        self.series = QPieSeries()
        for item in data:
            self.series.append(item['name'], item['quantity'])

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
        
        # Kết nối sự kiện hover của mỗi slice với một slot tùy chỉnh
        self.setup_hover_events()
        slice = QPieSlice()

        self.show()

    def setup_hover_events(self):
        for slice in self.series.slices():
            slice.hovered.connect(self.on_slice_hovered)

    def on_slice_hovered(self, state):
        now_slice = self.sender()
        if state:
            # Slice đang được hover
            print(f"Hovering over slice: {now_slice.label()}")
            slice = self.series.slices()[self.series.slices().index(now_slice)]
            slice.setExploded(True)
            slice.setLabelVisible(True)
        else:
            # Slice không còn được hover
            slice = self.series.slices()[self.series.slices().index(now_slice)]
            slice.setExploded(False)
            slice.setLabelVisible(False)

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
window = Ui()
app.exec()
