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
from PIL import Image, ImageOps
from io import BytesIO
import random
import string
import os

# Data
import urllib.request
from functools import partial
import unidecode
import shutil
import json

class Login(QMainWindow):
    # Setup
    image = ImageCaptcha(width=280, height=90, fonts=[])
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    image.write(captcha_text, 'Image//captcha.png')
    image = Image.open('Image//captcha.png')
    pixel_color = '#%02x%02x%02x' % image.getpixel((0, 0))

    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//login.ui', self)

        # Font
        font = QFont("Segoe UI", 10)
        font.setBold(True)
        self.label_7.setFont(font)
    
        # Captcha
        self.label.setPixmap(QtGui.QPixmap("Image//captcha.png"))
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
        self.image.write(self.captcha_text, 'Image//captcha.png')
        self.image = Image.open('Image//captcha.png')
        self.pixel_color = '#%02x%02x%02x' % self.image.getpixel((0, 0))
        self.label.setPixmap(QtGui.QPixmap("Image//captcha.png"))
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
        uic.loadUi('GUI//register.ui', self)
    
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
        uic.loadUi('GUI//user.ui', self)
        self.stackedWidget.setCurrentIndex(0)

        # Action
        self.btn_home.clicked.connect(self.go_to_home_screen)
        self.btn_shopping.clicked.connect(self.go_to_shopping_screen)
        self.btn_cart.clicked.connect(self.go_to_cart_screen)
        self.btn_setting.clicked.connect(self.go_to_setting_screen)
        self.btn_log_out.clicked.connect(self.log_out)

#!########################################### PRODUCT ############################################

    #! Product Store
        self.product_layout = QtWidgets.QGridLayout()  # Tạo QGridLayout để chứa các sản phẩm
        self.product_widget = QtWidgets.QWidget()  # Tạo QWidget để chứa QGridLayout
        self.product_widget.setLayout(self.product_layout)  # Đặt QGridLayout làm layout cho QWidget
        
        # Tạo QScrollArea và đặt QWidget làm nội dung cuộn
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.product_widget)

        # Đặt QScrollArea làm giao diện chính cho QWidget
        self.frame.setLayout(QtWidgets.QVBoxLayout())
        self.frame.layout().addWidget(self.scroll_area)

    #! Product Cart
        self.product_cart_layout = QtWidgets.QGridLayout()  # Tạo QGridLayout để chứa các san pham trong giỏ hàng
        self.product_cart_widget = QtWidgets.QWidget()  # Tạo QWidget để chứa QGridLayout
        self.product_cart_widget.setLayout(self.product_cart_layout)  # Đặt QGridLayout làm layout cho QWidget
        
        # Tạo QScrollArea và đặt QWidget làm nội dung cuộn
        self.scroll_area_cart = QtWidgets.QScrollArea()
        self.scroll_area_cart.setWidgetResizable(True)
        self.scroll_area_cart.setWidget(self.product_cart_widget)

        # Đặt QScrollArea làm giao diện chính cho QWidget
        self.frame_3.setLayout(QtWidgets.QVBoxLayout())
        self.frame_3.layout().addWidget(self.scroll_area_cart)
        
    #! Hiển thị tất cả các sản phẩm
        self.display_all_products_store(None)
        self.display_all_products_cart(None)
    
    def display_all_products_cart(self, information):
        # Lấy dữ liệu 
        if information:
            products_cart = information
        else:
            products_cart = json.load(open('cart_product.json'))
        
        # Hiển thị các sản phẩm trên giao diện
        row = 0
        col = 0
        for product in products_cart:
            widget_of_all = QtWidgets.QFrame()
            layout_of_all = QtWidgets.QHBoxLayout(widget_of_all)

            # width = 300
            height = 200
            # widget_of_all.setFixedSize(width, height)
            widget_of_all.setFixedHeight(height)

            #TODO: ẢNH
            #* Hiển thị ảnh
            image_path = product['image']  # Đường dẫn ảnh
            image_label = QtWidgets.QLabel()
            image_label.setStyleSheet("border: none")

            #! Lấy hình ảnh
            image_pixmap = QtGui.QPixmap(image_path)

            #! Resize ảnh
            image_pixmap = image_pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            #! Hiển thị ảnh
            image_label.setPixmap(image_pixmap)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_of_all.addWidget(image_label)

            #* Tạo Widget bao gồm tên và giá của sản phẩm
            product_information_widget = QtWidgets.QWidget()
            product_information_layout = QtWidgets.QVBoxLayout(product_information_widget)
            product_information_widget.setStyleSheet("border: none;")

            #* FONT
            font = QFont("Segoe UI", 15)
            font.setBold(True)
            font.setHintingPreference(QFont.HintingPreference.PreferFullHinting)
            
            # Hiển thị tên sản phẩm
            product_name_label = QtWidgets.QLabel(product['product_name'])
            product_name_label.setFont(font)
            product_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(product_name_label)
            
            # Hiển thị giá
            price_format = "{:,}".format(int(product["price"]))
            price_format = f"{price_format}₫"
            price_label = QtWidgets.QLabel(f"Giá: {price_format}")
            price_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(price_label)

            # Hiển thị danh mục
            category_label = QtWidgets.QLabel(f"Danh mục: {product['category']}")
            category_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(category_label)

            # Thêm nút "Show details"
            show_details_button = QtWidgets.QPushButton("Xem sản phẩm")
            show_details_button.clicked.connect(partial(self.display_product_details, product))
            show_details_button.setStyleSheet("background-color: white; padding: 6px; border-radius: 5px; border: 2px solid #dbdbdb; max-height: 20px; min-height: 20px;")
            product_information_layout.addWidget(show_details_button)
            layout_of_all.addWidget(product_information_widget)
            widget_of_all.setStyleSheet("background-color: white; border-radius : 15px; margin: 3px; border: 2px solid #dbdbdb;")

            # Thêm sản phẩm vào layout
            self.product_cart_layout.addWidget(widget_of_all, row, col)
            
            col += 1
            if col == 2:
                col = 0
                row += 1

    def display_all_products_store(self, information):
        # Lấy dữ liệu 
        if information:
            products = information
        else:
            products = json.load(open('product.json'))

        # Hiển thị các sản phẩm trên giao diện
        row = 0
        col = 0
        for product in products:
            widget_of_all = QtWidgets.QFrame()
            layout_of_all = QtWidgets.QHBoxLayout(widget_of_all)

            # width = 300
            height = 200
            # widget_of_all.setFixedSize(width, height)
            widget_of_all.setFixedHeight(height)

            #TODO: ẢNH
            #* Hiển thị ảnh
            image_path = product['image']  # Đường dẫn ảnh
            image_label = QtWidgets.QLabel()
            image_label.setStyleSheet("border: none")

            #! Lấy hình ảnh
            image_pixmap = QtGui.QPixmap(image_path)

            #! Resize ảnh
            image_pixmap = image_pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            #! Hiển thị ảnh
            image_label.setPixmap(image_pixmap)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_of_all.addWidget(image_label)

            #* Tạo Widget bao gồm tên và giá của sản phẩm
            product_information_widget = QtWidgets.QWidget()
            product_information_layout = QtWidgets.QVBoxLayout(product_information_widget)
            product_information_widget.setStyleSheet("border: none;")

            #* FONT
            font = QFont("Segoe UI", 15)
            font.setBold(True)
            font.setHintingPreference(QFont.HintingPreference.PreferFullHinting)
            
            # Hiển thị tên sản phẩm
            product_name_label = QtWidgets.QLabel(product['product_name'])
            product_name_label.setFont(font)
            product_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(product_name_label)
            
            # Hiển thị giá
            price_format = "{:,}".format(int(product["price"]))
            price_format = f"{price_format}₫"
            price_label = QtWidgets.QLabel(f"Giá: {price_format}")
            price_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(price_label)

            # Hiển thị danh mục
            category_label = QtWidgets.QLabel(f"Danh mục: {product['category']}")
            category_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(category_label)

            # Thêm nút "Show details"
            show_details_button = QtWidgets.QPushButton("Xem sản phẩm")
            show_details_button.clicked.connect(partial(self.display_product_details, product))
            show_details_button.setStyleSheet("background-color: white; padding: 6px; border-radius: 5px; border: 2px solid #dbdbdb; max-height: 20px; min-height: 20px;")
            product_information_layout.addWidget(show_details_button)
            layout_of_all.addWidget(product_information_widget)
            widget_of_all.setStyleSheet("background-color: white; border-radius : 15px; margin: 3px; border: 2px solid #dbdbdb;")

            # Thêm sản phẩm vào layout
            self.product_layout.addWidget(widget_of_all, row, col)
            
            col += 1
            if col == 2:
                col = 0
                row += 1
    
    def display_product_details(self, product):
        show_product_ui.show_product_information(product)
        show_product_ui.show()
    
    #! Switch screen
    def go_to_home_screen(self): 
        self.stackedWidget.setCurrentIndex(0)
        self.btn_home.setIcon(QIcon("Image//home_a.png"))
        self.btn_shopping.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_cart.setIcon(QIcon("Image//cart_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_shopping_screen(self): 
        self.stackedWidget.setCurrentIndex(1)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_shopping.setIcon(QIcon("Image//shopping_a.png"))
        self.btn_cart.setIcon(QIcon("Image//cart_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_cart_screen(self): 
        self.stackedWidget.setCurrentIndex(2)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_shopping.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_cart.setIcon(QIcon("Image//cart_a.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_setting_screen(self): 
        self.stackedWidget.setCurrentIndex(3)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_shopping.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_cart.setIcon(QIcon("Image//cart_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_a.png"))

    def log_out(self):
        login_ui.show()
        self.hide()
    
class Admin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//admin.ui', self)
        self.stackedWidget.setCurrentIndex(0)

        # Import json
        with open("Data//categorys.json", "r") as f:
            data = json.load(f)
        
        # Tạo dữ liệu cho biểu đồ Pie Chart
        self.series = QPieSeries()
        for item in data:
            self.series.append(item['name'], item['product'])

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

        self.btn_home.clicked.connect(self.go_to_home_screen)
        self.btn_product.clicked.connect(self.go_to_product_screen)
        self.btn_statistic.clicked.connect(self.go_to_statistic_screen)
        self.btn_setting.clicked.connect(self.go_to_setting_screen)
        self.btn_log_out.clicked.connect(self.log_out)

        self.product_layout = QtWidgets.QGridLayout()  # Tạo QGridLayout để chứa các sản phẩm
        self.product_widget = QtWidgets.QWidget()  # Tạo QWidget để chứa QGridLayout
        self.product_widget.setLayout(self.product_layout)  # Đặt QGridLayout làm layout cho QWidget
        
        # Tạo QScrollArea và đặt QWidget làm nội dung cuộn
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.product_widget)

        # Đặt QScrollArea làm giao diện chính cho QWidget
        self.frame.setLayout(QtWidgets.QVBoxLayout())
        self.frame.layout().addWidget(self.scroll_area)

        self.display_all_products(None)
    
    def display_all_products(self, information):
        # Lấy dữ liệu 
        if information:
            products = information
        else:
            products = json.load(open('product.json'))

        # Hiển thị các sản phẩm trên giao diện
        row = 0
        col = 0
        for product in products:
            widget_of_all = QtWidgets.QFrame()
            layout_of_all = QtWidgets.QHBoxLayout(widget_of_all)

            # width = 300
            height = 205
            # widget_of_all.setFixedSize(width, height)
            widget_of_all.setFixedHeight(height)

            #TODO: ẢNH
            #* Hiển thị ảnh
            image_path = product['image']  # Đường dẫn ảnh
            image_label = QtWidgets.QLabel()
            image_label.setStyleSheet("border: none")

            #! Lấy hình ảnh
            image_pixmap = QtGui.QPixmap(image_path)

            #! Resize ảnh
            image_pixmap = image_pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            #! Hiển thị ảnh
            image_label.setPixmap(image_pixmap)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_of_all.addWidget(image_label)

            #* Tạo Widget bao gồm tên và giá của sản phẩm
            product_information_widget = QtWidgets.QWidget()
            product_information_layout = QtWidgets.QVBoxLayout(product_information_widget)
            product_information_widget.setStyleSheet("border: none;")

            #* FONT
            font = QFont("Segoe UI", 15)
            font.setBold(True)
            font.setHintingPreference(QFont.HintingPreference.PreferFullHinting)
            
            # Hiển thị tên sản phẩm
            product_name_label = QtWidgets.QLabel(product['product_name'])
            product_name_label.setFont(font)
            product_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(product_name_label)
            
            # Hiển thị giá
            price_format = "{:,}".format(int(product["price"]))
            price_format = f"{price_format}₫"
            price_label = QtWidgets.QLabel(f"Giá: {price_format}")
            price_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(price_label)

            # Hiển thị danh mục
            category_label = QtWidgets.QLabel(f"Danh mục: {product['category']}")
            category_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(category_label)

            # Thêm nút "Chỉnh sửa"
            show_edit_button = QtWidgets.QPushButton("Chỉnh sửa")
            show_edit_button.clicked.connect(partial(self.display_product_edit, product))
            show_edit_button.setStyleSheet("background-color: yellow; padding: 6px; border-radius: 5px; border: 2px solid white; max-height: 20px; min-height: 20px;")
            product_information_layout.addWidget(show_edit_button)

            # Thêm nút "Xóa"
            show_delete_button = QtWidgets.QPushButton("Xóa")
            show_delete_button.clicked.connect(partial(self.display_product_details, product))
            show_delete_button.setStyleSheet("background-color: red; padding: 6px; border-radius: 5px; border: 2px solid white; max-height: 20px; min-height: 20px;")
            product_information_layout.addWidget(show_delete_button)
            
            # Thêm widget vào layout
            layout_of_all.addWidget(product_information_widget)
            
            # Đặt Stylesheet cho widget
            widget_of_all.setStyleSheet("background-color: white; border-radius: 15px; margin: 3px; border: 2px solid #dbdbdb;")

            # Thêm sản phẩm vào layout
            self.product_layout.addWidget(widget_of_all, row, col)
            
            col += 1
            if col == 2:
                col = 0
                row += 1
    
    def display_product_details(self, product):
        show_product_ui.show_product_information(product)
        show_product_ui.show()
    
    def display_product_edit(self, product):
        edit_product_ui.edit_product(product)
        information_product_ui.show()
        
    #! Switch screen
    def go_to_home_screen(self): 
        self.stackedWidget.setCurrentIndex(0)
        self.btn_home.setIcon(QIcon("Image//home_a.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_product_screen(self): 
        self.stackedWidget.setCurrentIndex(1)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_a.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_statistic_screen(self): 
        self.stackedWidget.setCurrentIndex(2)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_a.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_setting_screen(self): 
        self.stackedWidget.setCurrentIndex(3)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_a.png"))

    def log_out(self):
        login_ui.show()
        self.hide()

class Add_Product(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//addproduct.ui', self)

        self.image.setPixmap(QPixmap("Image//add_image.png").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.image_path = ""

        # Font
        label_font = QFont("Segoe UI", 18)
        label_font.setBold(True)

        title_font = QFont("Segoe UI", 14)
        title_font.setBold(True)

        btn_font = QFont("Segoe UI", 11)
        btn_font.setBold(True)

        bold = QFont("Times New Roman", 11)
        bold.setBold(True)

        italic = QFont("Times New Roman", 11)
        italic.setItalic(True)

        underline = QFont("Times New Roman", 11)
        underline.setUnderline(True)

        increase_and_decrease = QFont("Times New Roman", 11)
        increase_and_decrease.setBold(True)

        # UI set font
        self.l_title.setFont(label_font)
        self.name.setFont(title_font)
        self.price.setFont(title_font)
        self.tag.setFont(title_font)
        self.discription.setFont(title_font)

        self.bold.setFont(bold)
        self.italic.setFont(italic)
        self.underline.setFont(underline)
        self.increase.setFont(increase_and_decrease)
        self.decrease.setFont(increase_and_decrease)

        self.cancel.setFont(btn_font)
        self.add.setFont(btn_font)
        self.choose_image.setFont(btn_font)
        self.choose_image_url.setFont(btn_font)

        # Action
        self.bold.clicked.connect(self.setBold)
        self.italic.clicked.connect(self.setItalic)
        self.underline.clicked.connect(self.setUnderline)
        self.increase.clicked.connect(self.setIncrease)
        self.decrease.clicked.connect(self.setDecrease)
        self.choose_image.clicked.connect(self.chooseImage)
        self.choose_image_url.clicked.connect(self.choose_image_from_url)
        self.add.clicked.connect(self.add_new_product)
    

    def choose_image_from_url(self):
        url = QInputDialog.getText(self, "Nhập URL", "Nhập liên kết hình ảnh")[0]
        print(url)
        try: urllib.request.urlretrieve(url, "Image//temp_downloaded_file.jpg")
        except Exception as e: pass
        else: 

            self.image_path = "Image//temp_downloaded_file.jpg"

            #! Crop ảnh
            image_pixmap = QtGui.QPixmap(self.image_path)
            # check null image
            if not image_pixmap.isNull():
                original_width = image_pixmap.width()
                original_height = image_pixmap.height()
                new_width = image_pixmap.height()
                x = (original_width - new_width) // 2
                y = 0
                image_pixmap = image_pixmap.copy(x, y, new_width, original_height)

                #! Resize ảnh (Sau khi crop)
                image_pixmap = image_pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

                # Hiển thị Pixmap
                self.image.setPixmap(image_pixmap)
            else:
                self.image.setPixmap(QPixmap("Image//add_image.png").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                QMessageBox.warning(self, "Lỗi", "Gặp lỗi trong quá trình lấy hình ảnh")


    def setBold(self):
        cursor = self.textEdit.textCursor()
        format_bold = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if current_format.fontWeight() == QFont.Weight.Normal:
                format_bold.setFontWeight(QFont .Weight.Bold)
                cursor.mergeCharFormat(format_bold)
            else:
                format_bold.setFontWeight(QFont.Weight.Normal)
                cursor.mergeCharFormat(format_bold)
        self.textEdit.setTextCursor(cursor)
        
    def setItalic(self):
        cursor = self.textEdit.textCursor() # Lấy chuỗi đang được chọn
        format_italic = QTextCharFormat() # QTextCharFormat để thay đổi độ dày, in đậm, nghiêng chữ

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if current_format.fontItalic() == False:
                format_italic.setFontItalic(True)
                cursor.mergeCharFormat(format_italic) # Thay đổi chuỗi đang được chọn
            elif current_format.fontItalic() == True:
                format_italic.setFontItalic(False)
                cursor.mergeCharFormat(format_italic) # Thay đổi chuỗi đang được chọn
        self.textEdit.setTextCursor(cursor)

    def setUnderline(self):
        cursor = self.textEdit.textCursor()
        format_underline = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if not current_format.fontUnderline():
                format_underline.setFontUnderline(True)
                cursor.mergeCharFormat(format_underline)
            else:
                format_underline.setFontUnderline(False)
                cursor.mergeCharFormat(format_underline)
        self.textEdit.setTextCursor(cursor)

    def setIncrease(self):
        cursor = self.textEdit.textCursor()
        format_font = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_font = current_format.font()
            font_size = current_font.pointSize()
            if font_size < 73:
                font_size += 1
                new_font = QFont(current_font)
                new_font.setPointSize(font_size)
                format_font.setFont(new_font)
                cursor.mergeCharFormat(format_font)

        self.textEdit.setTextCursor(cursor)

    def setDecrease(self):
        cursor = self.textEdit.textCursor()
        format_font = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_font = current_format.font()
            font_size = current_font.pointSize()
            if font_size > 6:
                font_size -= 1
                new_font = QFont(current_font)
                new_font.setPointSize(font_size)
                format_font.setFont(new_font)
                cursor.mergeCharFormat(format_font)

        self.textEdit.setTextCursor(cursor)
    
    def chooseImage(self):
        #! Lấy đường dẫn đến ảnh
        self.image_path = QFileDialog.getOpenFileName(self, 'Add Image', "", "Images (*.png *.jpg *.jpeg *.jfif *.pjpeg *.pjp *.svg *.webp)")[0]

        if self.image_path:
            #! Crop ảnh
            image_pixmap = QtGui.QPixmap(self.image_path)
            original_width = image_pixmap.width()
            original_height = image_pixmap.height()
            new_width = image_pixmap.height()
            x = (original_width - new_width) // 2
            y = 0
            image_pixmap = image_pixmap.copy(x, y, new_width, original_height)

            #! Resize ảnh (Sau khi crop)
            image_pixmap = image_pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            # Hiển thị Pixmap
            self.image.setPixmap(image_pixmap)
        
    def add_new_product(self):
        print("Add product")
        self.l_title.setText("Thêm sản phẩm")
        self.add.setText("Thêm")

        name = self.line_name.text()
        price = self.line_price.text()
        # No inputmask
        description = self.textEdit.toPlainText()
        image_path = self.image_path
        tag = self.tag_name.currentText()
        simple_name = unidecode.unidecode(name)
        simple_name.replace(" ", "_")
        simple_name.lower()
        
        existing_data = json.load(open("product.json"))
        
        shutil.copyfile(image_path, f"Image//{name.lower().replace(' ', '_')}.png")
        
        new_product = {
            "simple_name": simple_name,
            "product_name": name,
            "price": price,
            "category": tag,
            "description": description,
            "image": f"Image//{name.lower().replace(' ', '_')}.png"
        }
        
        existing_data.append(new_product)
        product_file = open("product.json", "w", encoding="utf-8")
        product_file.write(json.dumps(existing_data, indent=4, ensure_ascii=False))
        user_ui.display_all_products_store(existing_data)
        self.close()

    def edit_product(self, product):
        print("Edit product")
        self.l_title.setText("Sửa sản phẩm")
        self.add.setText("Hoàn thành")

        self.line_name.setText(product["product_name"])
        self.line_price.setText(str(product["price"]))
        self.textEdit.setText(product["description"])
        self.image.setPixmap(QPixmap(product["image"]).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.tag_name.setCurrentText(product["category"])

class Edit_product(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//editproduct.ui', self)
        self.image.setPixmap(QPixmap("Image//add_image.png").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.image_path = ""

        # Font
        label_font = QFont("Segoe UI", 18)
        label_font.setBold(True)

        title_font = QFont("Segoe UI", 14)
        title_font.setBold(True)

        btn_font = QFont("Segoe UI", 11)
        btn_font.setBold(True)

        bold = QFont("Times New Roman", 11)
        bold.setBold(True)

        italic = QFont("Times New Roman", 11)
        italic.setItalic(True)

        underline = QFont("Times New Roman", 11)
        underline.setUnderline(True)

        increase_and_decrease = QFont("Times New Roman", 11)
        increase_and_decrease.setBold(True)

        # UI set font
        self.l_title.setFont(label_font)
        self.name.setFont(title_font)
        self.price.setFont(title_font)
        self.tag.setFont(title_font)
        self.discription.setFont(title_font)

        self.bold.setFont(bold)
        self.italic.setFont(italic)
        self.underline.setFont(underline)
        self.increase.setFont(increase_and_decrease)
        self.decrease.setFont(increase_and_decrease)

        self.cancel.setFont(btn_font)
        self.add.setFont(btn_font)
        self.choose_image.setFont(btn_font)
        self.choose_image_url.setFont(btn_font)

        # Action
        self.bold.clicked.connect(self.setBold)
        self.italic.clicked.connect(self.setItalic)
        self.underline.clicked.connect(self.setUnderline)
        self.increase.clicked.connect(self.setIncrease)
        self.decrease.clicked.connect(self.setDecrease)
        self.choose_image.clicked.connect(self.chooseImage)
        self.choose_image_url.clicked.connect(self.choose_image_from_url)
        self.add.clicked.connect(self.add_new_product)
    

    def choose_image_from_url(self):
        url = QInputDialog.getText(self, "Nhập URL", "Nhập liên kết hình ảnh")[0]
        print(url)
        try: urllib.request.urlretrieve(url, "Image//temp_downloaded_file.jpg")
        except Exception as e: pass
        else: 

            self.image_path = "Image//temp_downloaded_file.jpg"

            #! Crop ảnh
            image_pixmap = QtGui.QPixmap(self.image_path)
            # check null image
            if not image_pixmap.isNull():
                original_width = image_pixmap.width()
                original_height = image_pixmap.height()
                new_width = image_pixmap.height()
                x = (original_width - new_width) // 2
                y = 0
                image_pixmap = image_pixmap.copy(x, y, new_width, original_height)

                #! Resize ảnh (Sau khi crop)
                image_pixmap = image_pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

                # Hiển thị Pixmap
                self.image.setPixmap(image_pixmap)
            else:
                self.image.setPixmap(QPixmap("Image//add_image.png").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                QMessageBox.warning(self, "Lỗi", "Gặp lỗi trong quá trình lấy hình ảnh")


    def setBold(self):
        cursor = self.textEdit.textCursor()
        format_bold = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if current_format.fontWeight() == QFont.Weight.Normal:
                format_bold.setFontWeight(QFont .Weight.Bold)
                cursor.mergeCharFormat(format_bold)
            else:
                format_bold.setFontWeight(QFont.Weight.Normal)
                cursor.mergeCharFormat(format_bold)
        self.textEdit.setTextCursor(cursor)
        
    def setItalic(self):
        cursor = self.textEdit.textCursor() # Lấy chuỗi đang được chọn
        format_italic = QTextCharFormat() # QTextCharFormat để thay đổi độ dày, in đậm, nghiêng chữ

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if current_format.fontItalic() == False:
                format_italic.setFontItalic(True)
                cursor.mergeCharFormat(format_italic) # Thay đổi chuỗi đang được chọn
            elif current_format.fontItalic() == True:
                format_italic.setFontItalic(False)
                cursor.mergeCharFormat(format_italic) # Thay đổi chuỗi đang được chọn
        self.textEdit.setTextCursor(cursor)

    def setUnderline(self):
        cursor = self.textEdit.textCursor()
        format_underline = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if not current_format.fontUnderline():
                format_underline.setFontUnderline(True)
                cursor.mergeCharFormat(format_underline)
            else:
                format_underline.setFontUnderline(False)
                cursor.mergeCharFormat(format_underline)
        self.textEdit.setTextCursor(cursor)

    def setIncrease(self):
        cursor = self.textEdit.textCursor()
        format_font = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_font = current_format.font()
            font_size = current_font.pointSize()
            if font_size < 73:
                font_size += 1
                new_font = QFont(current_font)
                new_font.setPointSize(font_size)
                format_font.setFont(new_font)
                cursor.mergeCharFormat(format_font)

        self.textEdit.setTextCursor(cursor)

    def setDecrease(self):
        cursor = self.textEdit.textCursor()
        format_font = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_font = current_format.font()
            font_size = current_font.pointSize()
            if font_size > 6:
                font_size -= 1
                new_font = QFont(current_font)
                new_font.setPointSize(font_size)
                format_font.setFont(new_font)
                cursor.mergeCharFormat(format_font)

        self.textEdit.setTextCursor(cursor)
    
    def chooseImage(self):
        #! Lấy đường dẫn đến ảnh
        self.image_path = QFileDialog.getOpenFileName(self, 'Add Image', "", "Images (*.png *.jpg *.jpeg *.jfif *.pjpeg *.pjp *.svg *.webp)")[0]

        if self.image_path:
            #! Crop ảnh
            image_pixmap = QtGui.QPixmap(self.image_path)
            original_width = image_pixmap.width()
            original_height = image_pixmap.height()
            new_width = image_pixmap.height()
            x = (original_width - new_width) // 2
            y = 0
            image_pixmap = image_pixmap.copy(x, y, new_width, original_height)

            #! Resize ảnh (Sau khi crop)
            image_pixmap = image_pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            # Hiển thị Pixmap
            self.image.setPixmap(image_pixmap)
        
    def add_new_product(self):
        print("Add product")
        self.l_title.setText("Thêm sản phẩm")
        self.add.setText("Thêm")

        name = self.line_name.text()
        price = self.line_price.text()
        # No inputmask
        description = self.textEdit.toPlainText()
        image_path = self.image_path
        tag = self.tag_name.currentText()
        simple_name = unidecode.unidecode(name)
        simple_name.replace(" ", "_")
        simple_name.lower()
        
        existing_data = json.load(open("product.json"))
        
        shutil.copyfile(image_path, f"Image//{name.lower().replace(' ', '_')}.png")
        
        new_product = {
            "simple_name": simple_name,
            "product_name": name,
            "price": price,
            "category": tag,
            "description": description,
            "image": f"Image//{name.lower().replace(' ', '_')}.png"
        }
        
        existing_data.append(new_product)
        product_file = open("product.json", "w", encoding="utf-8")
        product_file.write(json.dumps(existing_data, indent=4, ensure_ascii=False))
        user_ui.display_all_products_store(existing_data)
        self.close()

    def edit_product(self, product):
        print("Edit product")
        self.l_title.setText("Sửa sản phẩm")
        self.add.setText("Hoàn thành")

        self.line_name.setText(product["product_name"])
        self.line_price.setText(str(product["price"]))
        self.textEdit.setText(product["description"])
        self.image.setPixmap(QPixmap(product["image"]).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.tag_name.setCurrentText(product["category"])


class Show_Product(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//show_product.ui', self)
        self.setStyleSheet("background-color: white; color: black")

        # Font
        name_font = QFont("Segoe UI", 18)
        name_font.setBold(True)

        category_font = QFont("Segoe UI", 13)

        price_font = QFont("Segoe UI", 17)
        price_font.setBold(True)

        description_label_font = QFont("Segoe UI", 16)
        description_label_font.setBold(True)

        btn_font = QFont("Segoe UI", 11)
        btn_font.setBold(True)

        # Set font
        self.name.setFont(name_font)
        self.category.setFont(category_font)
        self.price.setFont(price_font)
        self.add_button.setFont(btn_font)
        self.Description_label.setFont(description_label_font)

    def show_product_information(self, product):
        price_format = "{:,}".format(int(product["price"]))
        price_format = f"{price_format} ₫"
        self.image.setPixmap(QPixmap(product["image"]).scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.name.setText(product["product_name"])
        self.category.setText(product["category"])
        self.price.setText(price_format)
        self.Description.setText(product["description"])
        self.add_button.clicked.connect(lambda: self.add_to_cart(product))

    def add_to_cart(self, product):
        existing_data = json.load(open('cart_product.json'))
        existing_data.append(product)

        product_file = open("cart_product.json", "w", encoding="utf-8")
        product_file.write(json.dumps(existing_data, indent=4, ensure_ascii=False))
        
        user_ui.display_all_products_cart(existing_data)
        self.close()


app = QApplication(sys.argv)

# UI
login_ui = Login()
register_ui = Register()
show_product_ui = Show_Product()

information_product_ui = Add_Product()
edit_product_ui = Edit_product()

user_ui = User()
admin_ui = Admin()

# Setup
admin_ui.show()
app.exec()

try:
    os.remove("Image//captcha.png")
    os.remove("Image//temp_downloaded_file.jpg")
except Exception as e:
    pass