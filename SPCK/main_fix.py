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
from functools import partial
import urllib.request
import unidecode
import shutil
import json
import re

class Login(QMainWindow):
    # Setup
    font_path = "Image/FiraMonoNerdFont-Regular.otf"
    image = ImageCaptcha(width=280, height=90, fonts=[font_path])
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    image.write(captcha_text, 'Image//captcha.png')
    the_image = Image.open('Image//captcha.png')
    pixel_color = '#%02x%02x%02x' % the_image.getpixel((0, 0))

    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//login.ui', self)
        self.accounts = []

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
        self.load_account()
    
    def register(self):
        register_ui.show()
        login_ui.hide()
    
    def load_account(self):
        self.accounts = json.load(open("Data/account.json"))

    def regenerate_captcha(self):
        self.image = ImageCaptcha(width=280, height=90, fonts=['times'])
        self.captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.image.write(self.captcha_text, 'Image//captcha.png')
        self.image = Image.open('Image//captcha.png')
        self.pixel_color = '#%02x%02x%02x' % self.image.getpixel((0, 0))
        self.label.setPixmap(QtGui.QPixmap("Image//captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")
    
    def the_button_was_clicked(self):
        if self.email.text().replace(" ", "") == "" or self.password.text().replace(" ", "") == "" or self.captcha.text().replace(" ", "") == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Cảnh báo")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Vui lòng nhập đầy đủ thông tin!")
            msg_box.exec()

        else:
            if self.captcha.text() == self.captcha_text:
                for idx in range(len(self.accounts)):
                    if self.email.text() == self.accounts[idx]["email"] and self.password.text() == self.accounts[idx]["password"]:
                        a = self.accounts[idx]["user_name"]
                        print(f"Data/Cart_product/{a}.json")
                        user_ui.json_product_file = f"Data/Cart_product/{a}.json"
                        user_ui.reload_cart_interface()
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Thành công")
                        msg_box.setText("Đăng nhập thành công")
                        msg_box.exec()
                        self.close()
                        user_ui.show()
                        break

                    elif idx == len(self.accounts)-1:
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Cảnh báo")
                        msg_box.setIcon(QMessageBox.Icon.Warning)
                        msg_box.setText("Thông tin tài khoản không chính xác")
                        msg_box.exec()
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Cảnh báo")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Mã Captcha không chính xác")
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
    
    def check_string(self, string):
        print(string)
        has_digit = any(char.isdigit() for char in string)
        has_upper = any(char.isupper() for char in string)
        has_special = bool(re.search(r'[^\w\s]', string))
        if True in [has_digit, has_upper, has_special]:
            return True
        else:
            return False
    
    def login(self):
        login_ui.show()
        register_ui.hide()
    
    def the_button_was_clicked(self):
        if self.name.text().replace(" ", "") == "" or self.email.text().replace(" ", "") == "" or self.user_name.text().replace(" ", "") == "" or self.password.text().replace(" ", "") == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Lỗi")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_text = "Vui lòng điền vào tất cả các ô thông tin"
            msg_box.setText(msg_text)
            msg_box.exec()
        else:
            if self.check_string(self.user_name.text()):
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Cảnh báo")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Tên đăng nhập chỉ không được viết hoa,\nkhông được có kí tự đặc biệt và số")
                msg_box.exec()
            
            else:
                if self.checkBox.isChecked():
                    account = json.load(open("Data/account.json"))
                    if not any(acc["user_name"] == str(self.user_name.text()) for acc in account):
                        if not any(acc["email"] == str(self.email.text()) for acc in account):
                            account.append(
                                {
                                    "user_name": str(self.user_name.text()),
                                    "password": str(self.password.text()),
                                    "email": str(self.email.text()),
                                    "name": str(self.name.text())
                                })
                            json.dump(account, open("Data/account.json", "w"), indent=4, ensure_ascii=False)
                            json.dump([], open(f"Data/Cart_product/{self.user_name.text()}.json", "w"), indent=4, ensure_ascii=False)
                            login_ui.load_account()
                            msg_box = QMessageBox()
                            msg_box.setWindowTitle("Thành công")
                            msg_box.setIcon(QMessageBox.Icon.Information)
                            msg_text = "Tài khoản của bạn đã được tạo!"
                            msg_box.setText(msg_text)
                            msg_box.exec()
                        else:
                            msg_box = QMessageBox()
                            msg_box.setWindowTitle("Cảnh báo")
                            msg_box.setIcon(QMessageBox.Icon.Warning)
                            msg_text = "Email đã được sử dụng"
                            msg_box.setText(msg_text)
                            msg_box.exec()
                    else:
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Cảnh báo")
                        msg_box.setIcon(QMessageBox.Icon.Warning)
                        msg_text = "Tên đăng nhập đã tồn tại"
                        msg_box.setText(msg_text)
                        msg_box.exec()
                else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Cảnh báo")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setText("Vui lòng đồng ý các điều khoản")
                    msg_box.exec()

class User(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//user.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.json_product_file = "empty_cart_product.json"

        # Action
        self.btn_home.clicked.connect(self.go_to_home_screen)
        self.btn_shopping.clicked.connect(self.go_to_shopping_screen)
        self.btn_cart.clicked.connect(self.go_to_cart_screen)
        self.btn_setting.clicked.connect(self.go_to_setting_screen)
        self.btn_log_out.clicked.connect(self.log_out)
        self.search_btn.clicked.connect(lambda: self.search_product(self.search_line.text()))
        self.pushButton_23.clicked.connect(self.go_to_shopping_screen)
        self.pushButton_2.clicked.connect(lambda: self.search_product(self.lineEdit.text()))

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
        self.display_all_products_store()
        self.display_all_products_cart()

    #! Các phương thức quản lí sản phẩm
    def remove_cart_product(self, product):
        data = json.load(open(self.json_product_file))
        data.remove(product)
        print(data)
        json.dump(data, open(self.json_product_file, "w"), indent=4, ensure_ascii=False)
        self.reload_cart_interface()

    def reload_cart_interface(self):
        # Xóa tất cả các widget con của product_cart_layout
        while self.product_cart_layout.count():
            child = self.product_cart_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Hiển thị lại tất cả các sản phẩm
        self.display_all_products_cart()
    
    def display_all_products_cart(self):
        # Lấy dữ liệu 
        products_cart = json.load(open(self.json_product_file))
        
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
            show_details_button = QtWidgets.QPushButton("Xóa")
            show_details_button.clicked.connect(lambda: self.remove_cart_product(product))
            show_details_button.setStyleSheet("background-color: #FF320E; color: white; padding: 6px; border-radius: 5px; border: 2px solid black; max-height: 20px; min-height: 20px;")
            product_information_layout.addWidget(show_details_button)
            layout_of_all.addWidget(product_information_widget)
            widget_of_all.setStyleSheet("background-color: white; border-radius : 15px; margin: 3px; border: 2px solid #dbdbdb;")

            # Thêm sản phẩm vào layout
            self.product_cart_layout.addWidget(widget_of_all, row, col)
            
            col += 1
            if col == 2:
                col = 0
                row += 1
    
    def reload_store_interface(self):
        # Xóa tất cả các widget con của product_layout
        while self.product_layout.count():
            child = self.product_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Hiển thị lại tất cả các sản phẩm
        self.display_all_products_store()

    def display_all_products_store(self):
        # Lấy dữ liệu 
        products = json.load(open('product.json', encoding='utf-8'))

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

    def search_product(self, key_word):
        # Chuyển sang trang tìm kiếm với giao diện được đảm bảo
        self.go_to_shopping_screen()
        self.search_line.setText(key_word)

        # Xóa tất cả các widget con của product_cart_layout
        while self.product_layout.count():
            child = self.product_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Lấy dữ liệu
        products = json.load(open('product.json', encoding='utf-8'))

        # Tìm kiếm sản phẩm theo từ khóa
        row = 0
        col = 0
        for product in products:
            if unidecode.unidecode(key_word.lower()) in unidecode.unidecode(product['product_name']).lower():
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

    #! Thay đổi màn hình
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
        self.reload_store_interface()

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
        self.btn_home.setIcon(QIcon("Image//home_a.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))
        self.btn_catgory.setIcon(QIcon("Image//category_d.png"))

        #! Action
        self.btn_home.clicked.connect(self.go_to_home_screen)
        self.btn_product.clicked.connect(self.go_to_product_screen)
        self.btn_statistic.clicked.connect(self.go_to_statistic_screen)
        self.btn_catgory.clicked.connect(self.go_to_category_screen)
        self.btn_setting.clicked.connect(self.go_to_setting_screen)
        self.btn_log_out.clicked.connect(self.log_out)
        self.add_btn.clicked.connect(self.add_product)
        self.add_cg.clicked.connect(self.add_category)
        self.del_cg.clicked.connect(self.remove_category)

        #! Show product
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

        # Hiện sản phẩm
        self.display_all_products()

        #! Category
        self.categore_list = json.load(open('Data/categorys.json'))
        for categore in self.categore_list:
            self.cg_list.addItem(categore['name'])
        self.more_info.clicked.connect(self.show_more_info)

        # Create Pie Chart
        self.create_pie_chart()
    
    def create_pie_chart(self):
        
        # Xóa tất cả các widget con của layout hiện tại
        if self.pie_chart.layout() is not None:
            old_layout = self.pie_chart.layout()
            while old_layout.count():
                child = old_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            sip.delete(old_layout)  # Xóa layout cũ

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

    def reload_interface(self):
        # Xóa tất cả các widget con của product_layout
        while self.product_layout.count():
            child = self.product_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Hiển thị lại tất cả các sản phẩm
        self.display_all_products()
    
    def display_all_products(self):

        # Lấy dữ liệu
        products = json.load(open('product.json', encoding='utf-8'))

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
            show_delete_button.clicked.connect(partial(self.remove_product, product))
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

    def add_product(self):
        add_product_ui.show()
    
    def display_product_details(self, product):
        show_product_ui.show_product_information(product)
        show_product_ui.show()
    
    def display_product_edit(self, product):
        edit_product_ui.edit_product(product)
        edit_product_ui.show()

    def remove_product(self, product):
        data = json.load(open("product.json"))
        data.remove(product)
        print(data)
        json.dump(data, open("product.json", "w"), indent=4, ensure_ascii=False)
        os.remove(product["image"])
        admin_ui.fix_category()
        self.reload_interface()

    def add_category(self):
        # Get name of category with message box
        new_category,_ = QInputDialog.getText(self, "Thêm danh mục", "Nhập tên danh mục:")
        if new_category:
            self.cg_list.addItem(new_category)
            inp_data = json.load(open("Data/categorys.json"))
            inp_data.insert(0, {"name": new_category, "product": 0})
            json.dump(inp_data, open("Data/categorys.json", "w"), indent=4, ensure_ascii=False)
            self.create_pie_chart()
    
    def remove_category(self):
        self.cg_list.takeItem(self.cg_list.currentRow())
        inp_data = json.load(open("Data/categorys.json"))
        inp_data.pop(self.cg_list.currentRow())
        json.dump(inp_data, open("Data/categorys.json", "w"), indent=4, ensure_ascii=False)
        self.create_pie_chart()

    def show_more_info(self):
        inp_data = json.load(open("Data/categorys.json"))
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Thông tin")
        msg_box.setText(f"Tên danh mục: {inp_data[self.cg_list.currentRow()]['name']}\nSố sản phẩm: {inp_data[self.cg_list.currentRow()]['product']}")
        msg_box.exec()
    
    # def fix_category(self):
    #     json_product = json.load(open("product.json"))
    #     json_category = json.load(open("Data/categorys.json"))

    #     # Khởi tạo số lượng sản phẩm cho mỗi danh mục là 0
    #     for category in json_category:
    #         category["product"] = 0

    #     # Đếm số lượng sản phẩm cho mỗi danh mục
    #     for product in json_product:
    #         for category in json_category:
    #             if category["name"] == product["category"]:
    #                 category["product"] += 1

    #     # Ghi đồi file JSON
    #     json.dump(json_category, open("Data/categorys.json", "w"), indent=4, ensure_ascii=False)
    
    def fix_category(self):
        try:
            with open("product.json", "r", encoding="utf-8") as product_file:
                json_product = json.load(product_file)
            with open("Data/categorys.json", "r", encoding="utf-8") as category_file:
                json_category = json.load(category_file)
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
            return
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

        # Khởi tạo số lượng sản phẩm cho mỗi danh mục là 0
        for category in json_category:
            category["product"] = 0

        # Đếm số lượng sản phẩm cho mỗi danh mục
        for product in json_product:
            for category in json_category:
                if category["name"] == product["category"]:
                    category["product"] += 1

        # Ghi đồi file JSON
        try:
            with open("Data/categorys.json", "w", encoding="utf-8") as category_file:
                json.dump(json_category, category_file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error writing to category file: {e}")
        
        # Sửa bảng Pie Chart
        self.create_pie_chart()

    #! Switch screen
    def go_to_home_screen(self): 
        self.stackedWidget.setCurrentIndex(0)
        self.btn_home.setIcon(QIcon("Image//home_a.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_catgory.setIcon(QIcon("Image//category_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_product_screen(self): 
        self.stackedWidget.setCurrentIndex(1)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_a.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_catgory.setIcon(QIcon("Image//category_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_statistic_screen(self): 
        self.stackedWidget.setCurrentIndex(2)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_a.png"))
        self.btn_catgory.setIcon(QIcon("Image//category_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))
    
    def go_to_category_screen(self): 
        self.stackedWidget.setCurrentIndex(3)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_catgory.setIcon(QIcon("Image//category_a.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_d.png"))

    def go_to_setting_screen(self): 
        self.stackedWidget.setCurrentIndex(4)
        self.btn_home.setIcon(QIcon("Image//home_d.png"))
        self.btn_product.setIcon(QIcon("Image//shopping_d.png"))
        self.btn_statistic.setIcon(QIcon("Image//chart_bar_d.png"))
        self.btn_catgory.setIcon(QIcon("Image//category_d.png"))
        self.btn_setting.setIcon(QIcon("Image//setting_a.png"))

    def log_out(self):
        login_ui.show()
        self.close()

class Add_Product(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI//addproduct.ui', self)
        self.tag_name.addItems([item['name'] for item in json.load(open("Data/categorys.json"))])
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
        try: urllib.request.urlretrieve(url, "Image//temp_downloaded_file.png")
        except Exception as e: pass
        else: 

            self.image_path = "Image//temp_downloaded_file.png"

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
        self.l_title.setText("Thêm sản phẩm")
        self.add.setText("Thêm")

        name = self.line_name.text()
        price = self.line_price.text()
        
        # No inputmask
        description = self.textEdit.toPlainText()
        image_path = self.image_path
        tag = self.tag_name.currentText()
        simple_name = unidecode.unidecode(name).replace(" ", "_").lower()

        try:
            with open("product.json", "r", encoding="utf-8") as product_file:
                existing_data = json.load(product_file)
        except FileNotFoundError:
            existing_data = []
        except json.JSONDecodeError:
            print("Error decoding JSON from product.json. Initializing with empty list.")
            existing_data = []

        # Sao chép tệp ảnh
        try:
            shutil.copyfile(image_path, f"Image//{simple_name}.png")
        except FileNotFoundError as e:
            print(f"Image file not found: {e.filename}")
            return
        except Exception as e:
            print(f"Error copying image file: {e}")
            return

        new_product = {
            "product_name": name,
            "price": price,
            "category": tag,
            "description": description,
            "image": f"Image//{simple_name}.png"
        }

        existing_data.append(new_product)

        try:
            with open("product.json", "w", encoding="utf-8") as product_file:
                json.dump(existing_data, product_file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error writing to product.json: {e}")
            return

        print("Added")
        admin_ui.fix_category()
        admin_ui.reload_interface()
        self.close()

class Edit_product(QMainWindow):
    def __init__(self):
        super().__init__()

        self.product_edit = []
        self.product_input = []

        uic.loadUi('GUI//editproduct.ui', self)
        self.tag_name.addItems([item['name'] for item in json.load(open("Data/categorys.json"))])

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
        self.save.setFont(btn_font)
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
        self.save.clicked.connect(self.save_product)
        self.cancel.clicked.connect(self.close)
    

    def choose_image_from_url(self):
        url = QInputDialog.getText(self, "Nhập URL", "Nhập liên kết hình ảnh")[0]
        print(url)
        try:
            urllib.request.urlretrieve(url, "Image//new_edit_file.jpg")
        
        except Exception as e: 
            print(e)
        
        else:
            self.product_edit["image"] = "Image//new_edit_file.jpg"

            #! Crop ảnh
            image_pixmap = QtGui.QPixmap(self.product_edit["image"])
            # Check null image
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

            self.product_edit["image"] = self.image_path

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
        
    def save_product(self):
        print("Save product")

        data = json.load(open("product.json"))
        for product in data:
            if product["product_name"] == self.product_input["product_name"]:
                simple_name = unidecode.unidecode(self.line_name.text())
                simple_name.replace(" ", "_")
                simple_name.lower()
                product["product_name"] = self.line_name.text()
                product["price"] = self.line_price.text()
                product["category"] = self.tag_name.currentText()
                product["description"] = self.textEdit.toPlainText()
                try:
                    shutil.copyfile(self.product_edit["image"], f"Image//{self.line_name.text().lower().replace(' ', '_')}.png")
                except shutil.SameFileError:
                    pass
                else:
                    os.remove(self.product_input["image"])
                    product["image"] = f"Image//{self.line_name.text().lower().replace(' ', '_')}.png"
                with open("product.json", "w") as f: json.dump(data, f, indent=4, ensure_ascii=False)
                print("Saved")
                break

        admin_ui.fix_category()
        admin_ui.display_all_products()
        self.close()

    def edit_product(self, product):
        print("Edit product")
        print(product)

        self.product_edit = product
        self.product_input = product

        print(self.product_edit)
        self.line_name.setText(product["product_name"])
        self.line_price.setText(str(product["price"]))
        self.textEdit.setText(product["description"])
        self.image.setPixmap(QPixmap(product["image"]).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.tag_name.setCurrentText(product["category"])
        self.image_path = product["image"]

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

        try:
            self.add_button.clicked.disconnect()
        except TypeError:
            pass
        
        self.add_button.clicked.connect(lambda: self.add_to_cart(product))

    def add_to_cart(self, product_add):
        print("Product Add:")
        print(product_add)
        print()
        with open(user_ui.json_product_file, 'r') as f:
            data = json.load(f)
            print("import:")
            print(data)
        data.append(product_add)

        print("export:")
        print(data)
        print()

        with open(user_ui.json_product_file, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        user_ui.reload_cart_interface()
        self.close()


app = QApplication(sys.argv)

# UI
login_ui = Login()
register_ui = Register()
show_product_ui = Show_Product()

edit_product_ui = Edit_product()
add_product_ui = Add_Product()

user_ui = User()
admin_ui = Admin()

# Setup
login_ui.show()
app.exec()

try:
    os.remove("Image//captcha.png")
    os.remove("Image//temp_downloaded_file.png")
except Exception as e:
    pass