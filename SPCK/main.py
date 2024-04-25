# PyQt6
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtCharts import *
from PyQt6 import uic
import sys

# Captcha
from captcha.image import ImageCaptcha
from PIL import Image
import random
import string
import os

# Data
import json

class Login(QMainWindow):
    # Setup
    image = ImageCaptcha(width=280, height=90, fonts=['times'])
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    image.write(captcha_text, 'Image\\captcha.png')
    image = Image.open('Image\\captcha.png')
    pixel_color = '#%02x%02x%02x' % image.getpixel((0, 0))

    def __init__(self):
        super().__init__()
        uic.loadUi('GUI\\login.ui', self)

        # Font
        font = QFont("Segoe UI", 10)
        font.setBold(True)
        self.label_7.setFont(font)
    
        # Captcha
        self.label.setPixmap(QtGui.QPixmap("Image\\captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")

        # Action
        self.pushButton_2.clicked.connect(self.regenerate_captcha)
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.mousePressEvent = lambda event: self.register()
    
    def register(self):
        register_ui.show()
        login_ui.hide()

    def regenerate_captcha(self):
        self.image = ImageCaptcha(width=280, height=90, fonts=['times'])
        self.captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.image.write(self.captcha_text, 'Image\\captcha.png')
        self.image = Image.open('Image\\captcha.png')
        self.pixel_color = '#%02x%02x%02x' % self.image.getpixel((0, 0))
        self.label.setPixmap(QtGui.QPixmap("Image\\captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")
    
    def the_button_was_clicked(self):
        if self.lineEdit_3.text() == "admin@example.com" and self.lineEdit_2.text() == "admin" and self.lineEdit_4.text() == self.captcha_text:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thành công")
            msg_box.setText("Đăng nhập thành công")
            msg_box.exec()
            self.close()
            user_ui.show()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Cảnh báo")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Thông tin tài khoảng không chính xác")
            msg_box.exec()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI\\register.ui', self)
    
        font = QFont("Segoe UI", 10)
        font.setBold(True)
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.setFont(font)
        self.label_7.mousePressEvent = lambda event: self.login()
    
    def login(self):
        login_ui.show()
        register_ui.hide()
    
    def the_button_was_clicked(self):
        if self.lineEdit.text().replace(" ", "") == "" or self.lineEdit_2.text().replace(" ", "") == "" or self.lineEdit_3.text().replace(" ", "") == "" or self.lineEdit_4.text().replace(" ", "") == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Lỗi")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_text = "Vui lòng điền vào tất cả các ô thông tin"
            msg_box.setText(msg_text)
            msg_box.exec()
        else:
            if self.lineEdit_2.text() == self.lineEdit_4.text():
                if self.checkBox.isChecked():
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Thành công")
                    msg_text = "Tài khoản của bạn đã được tạo:\n" + f"Tên: {self.lineEdit.text()}\nEmail: {self.lineEdit_3.text()}\nMật khẩu: {self.lineEdit_2.text()}"
                    msg_box.setText(msg_text)
                    msg_box.exec()
                    self.close()
                    user_ui.show()
                else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Cảnh báo")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setText("Vui lòng đồng ý các điều khoản")
                    msg_box.exec()
            else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Caution")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setText("Mật khẩu không trùng khớp")
                    msg_box.exec()

class User(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI\\user.ui', self)
        self.stackedWidget.setCurrentIndex(0)

        # Action
        self.btn_home.clicked.connect(self.go_to_home_screen)
        self.btn_shopping.clicked.connect(self.go_to_shopping_screen)
        self.btn_cart.clicked.connect(self.go_to_cart_screen)
        self.btn_setting.clicked.connect(self.go_to_setting_screen)
        self.btn_log_out.clicked.connect(self.log_out)
    
    # Switch screen
    def go_to_home_screen(self): 
        self.stackedWidget.setCurrentIndex(0)
        self.btn_home.setIcon(QIcon("Image\\home_a.png"))
        self.btn_shopping.setIcon(QIcon("Image\\shopping_d.png"))
        self.btn_cart.setIcon(QIcon("Image\\cart_d.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_d.png"))

    def go_to_shopping_screen(self): 
        self.stackedWidget.setCurrentIndex(1)
        self.btn_home.setIcon(QIcon("Image\\home_d.png"))
        self.btn_shopping.setIcon(QIcon("Image\\shopping_a.png"))
        self.btn_cart.setIcon(QIcon("Image\\cart_d.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_d.png"))

    def go_to_cart_screen(self): 
        self.stackedWidget.setCurrentIndex(2)
        self.btn_home.setIcon(QIcon("Image\\home_d.png"))
        self.btn_shopping.setIcon(QIcon("Image\\shopping_d.png"))
        self.btn_cart.setIcon(QIcon("Image\\cart_a.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_d.png"))

    def go_to_setting_screen(self): 
        self.stackedWidget.setCurrentIndex(3)
        self.btn_home.setIcon(QIcon("Image\\home_d.png"))
        self.btn_shopping.setIcon(QIcon("Image\\shopping_d.png"))
        self.btn_cart.setIcon(QIcon("Image\\cart_d.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_a.png"))

    def log_out(self):
        login_ui.show()
        self.hide()
    
class Admin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI\\admin.ui', self)
        self.stackedWidget.setCurrentIndex(0)


############################################# PIE CHART #############################################
        # Import json
        with open("Data\\json.json", "r") as f:
            data = json.load(f)
        
        # Tạo dữ liệu cho biểu đồ Pie Chart
        self.series = QPieSeries()
        for item in data:
            self.series.append(item['name'], item['quantity'])
        
        # Đặt label của các slices là phần trăm
        # for slice in self.series.slices():
            # slice.setLabel("{:.2f}%".format(100 * slice.percentage()))

        # Tạo biểu đồ từ dữ liệu
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Bảng thống kê tỷ lệ sản phẩm bán ra theo từng nhóm")
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
        self.pie_chart.setLayout(layout)
        
        # Thuộc tính của biểu đồ Pie Chart
        for i in range(len(self.series.slices())):
            slice = QPieSlice()
            slice = self.series.slices()[i]
            # slice.setExploded(True)
            slice.setLabelVisible(True)


############################################# ACTION #############################################

        self.btn_home.clicked.connect(self.go_to_home_screen)
        self.btn_product.clicked.connect(self.go_to_product_screen)
        self.btn_statistic.clicked.connect(self.go_to_statistic_screen)
        self.btn_setting.clicked.connect(self.go_to_setting_screen)
        self.btn_log_out.clicked.connect(self.log_out)
    
######################################### SWITCH SCREEN #########################################
    def go_to_home_screen(self): 
        self.stackedWidget.setCurrentIndex(0)
        self.btn_home.setIcon(QIcon("Image\\home_a.png"))
        self.btn_product.setIcon(QIcon("Image\\shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image\\chart_bar_d.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_d.png"))

    def go_to_product_screen(self): 
        self.stackedWidget.setCurrentIndex(1)
        self.btn_home.setIcon(QIcon("Image\\home_d.png"))
        self.btn_product.setIcon(QIcon("Image\\shopping_a.png"))
        self.btn_statistic.setIcon(QIcon("Image\\chart_bar_d.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_d.png"))

    def go_to_statistic_screen(self): 
        self.stackedWidget.setCurrentIndex(2)
        self.btn_home.setIcon(QIcon("Image\\home_d.png"))
        self.btn_product.setIcon(QIcon("Image\\shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image\\chart_bar_a.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_d.png"))

    def go_to_setting_screen(self): 
        self.stackedWidget.setCurrentIndex(3)
        self.btn_home.setIcon(QIcon("Image\\home_d.png"))
        self.btn_product.setIcon(QIcon("Image\\shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image\\chart_bar_d.png"))
        self.btn_setting.setIcon(QIcon("Image\\setting_a.png"))

    def log_out(self):
        login_ui.show()
        self.hide()

app = QApplication(sys.argv)

# UI
login_ui = Login()
register_ui = Register()

user_ui = User()
admin_ui = Admin()

# Setup
admin_ui.show()
app.exec()
os.remove("Image\\captcha.png")