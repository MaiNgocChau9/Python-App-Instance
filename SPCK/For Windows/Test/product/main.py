from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from functools import partial
import json
import sys

class Display(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Test//product//ui.ui", self)
        
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
        
        # Hiển thị tất cả các sản phẩm
        self.display_all_products()

    def display_all_products(self):
        # Đọc dữ liệu từ file JSON
        products = json.load(open('Test/product/product.json', 'r', encoding='utf-8'))

        # Hiển thị các sản phẩm trên giao diện
        row = 0
        col = 0
        for product in products:
            product_widget = QtWidgets.QFrame()
            product_layout = QtWidgets.QHBoxLayout(product_widget)

            widget_of_all = QtWidgets.QFrame()
            layout_of_all = QtWidgets.QHBoxLayout(widget_of_all)
            
            # width = 300
            height = 200
            # widget_of_all.setFixedSize(width, height)
            widget_of_all.setFixedHeight(height)

            #TODO: ẢNH
            #* Hiển thị ảnh
            image_path = f"Test/product/image/{product['product_id']}.jpg"  # Đường dẫn ảnh
            image_label = QtWidgets.QLabel()
            image_label.setStyleSheet("border: none")

            #! Crop ảnh
            image_pixmap = QtGui.QPixmap(image_path)
            original_width = image_pixmap.width()
            original_height = image_pixmap.height()
            new_width = 200
            new_height = 200
            x = (original_width - new_width) // 2
            y = (original_height - new_height) // 2
            image_pixmap = image_pixmap.copy(x, y, new_width, new_height)

            #! Resize ảnh (Sau khi crop)
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
            price_label = QtWidgets.QLabel(f"Price: {product['price']}")
            price_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            product_information_layout.addWidget(price_label)
            """
            * Get font name of price_label
            price_label_font = price_label.font()
            print(price_label_font.family())
            """

            # Thêm nút "Show details"
            show_details_button = QtWidgets.QPushButton("Show details")
            show_details_button.clicked.connect(partial(self.display_product_details, product))
            show_details_button.setStyleSheet("background-color: white; padding: 6px; border-radius: 5px; border: 2px solid #dbdbdb; max-height: 20px; min-height: 20px;")
            product_information_layout.addWidget(show_details_button)
            product_information_widget.setStyleSheet("max-height: 150px; min-height: 50px; background-color: none;")
            layout_of_all.addWidget(product_information_widget)
            widget_of_all.setStyleSheet("background-color: white; border-radius : 15px; margin: 3px;")
            
            # Shadow
            # self.product_widget.setStyleSheet("background-color: white; color: black")
            shadow = QtWidgets.QGraphicsDropShadowEffect()
            shadow.setOffset(0, 0)
            shadow.setBlurRadius(20)
            shadow.setColor(QtGui.QColor("#e6e6e6"))
            self.product_widget.setGraphicsEffect(shadow)

            # Thêm sản phẩm vào layout
            self.product_layout.addWidget(widget_of_all, row, col)
            
            col += 1
            if col == 3:
                col = 0
                row += 1
    
    def display_product_details(self, product):
        
        # Tạo cửa sổ nhỏ để hiển thị chi tiết sản phẩm
        details_window = QtWidgets.QDialog(self)
        details_window.setWindowTitle("Product Details")

        # Tạo layout cho cửa sổ nhỏ
        details_layout = QtWidgets.QVBoxLayout(details_window)

        # Hiển thị chi tiết sản phẩm
        product_info_label = QtWidgets.QLabel(f"Product ID: {product['product_id']}")
        details_layout.addWidget(product_info_label)

        product_info_label = QtWidgets.QLabel(f"Product Name: {product['product_name']}")
        details_layout.addWidget(product_info_label)

        product_info_label = QtWidgets.QLabel(f"Category: {product['category']}")
        details_layout.addWidget(product_info_label)

        product_info_label = QtWidgets.QLabel(f"Quantity: {product['quantity']}")
        details_layout.addWidget(product_info_label)

        product_info_label = QtWidgets.QLabel(f"Price: {product['price']}")
        details_layout.addWidget(product_info_label)

        product_info_label = QtWidgets.QLabel(f"Import Date: {product['import_date']}")
        details_layout.addWidget(product_info_label)

        # Hiển thị cửa sổ nhỏ
        details_window.exec()

app = QtWidgets.QApplication(sys.argv)
main_ui = Display()
main_ui.show()
sys.exit(app.exec())