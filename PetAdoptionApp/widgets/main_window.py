from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import uic

from widgets.filters import Dog_Filter, Cat_Filter, Pet_Filter
from widgets.pets import Dog, Cat, Dog_Detail1


class SignalManager(QWidget):
    login_true = pyqtSignal(str)
    register_true = pyqtSignal(str)
    show_register_signal = pyqtSignal()
    show_login_signal = pyqtSignal()
    show_detail_signal = pyqtSignal()


# Lớp chứa giao diện chính
class MainWindow(QMainWindow):
    def __init__(self, signal_manager:SignalManager):
        super().__init__()
        self.ui = uic.loadUi("gui/main.ui", self)

        self.signal_manager = signal_manager
        # self.signal_manager.filter_signal.connect(self.show_filter)

        # Hiển thị bộ lọc danh sách dog
        self.ui.icon_dog.clicked.connect(self.show_dog)
        self.ui.btn_opt_dog.clicked.connect(self.show_dog)
        # Hiển thị bộ lọc danh sách cat
        self.ui.icon_cat.clicked.connect(self.show_cat)
        self.ui.btn_opt_cat.clicked.connect(self.show_cat)
        # Hiển thị bộ lọc danh sách các thú cưng khác
        self.ui.icon_other.clicked.connect(self.show_pet)
        self.ui.btn_opt_other.clicked.connect(self.show_pet)
        #Hiển thị thông tin thú cưng nổi bật
        self.ui.btn_dog.clicked.connect(self.show_dog_details)
        self.ui.btn_dogName.clicked.connect(self.show_dog_details)
        
    def on_login_successful(self, username):
        self.ui.lbUsername.setText(username)
        self.show()
    
    def on_register_successful(self, username):
        self.ui.lbUsername.setText(username)
        self.show()
    
    def show_dog(self):
        self.hide()
        dog = Dog(self.signal_manager, parent=self)
        dog_filter = Dog_Filter(parent=self, child=dog)
        dog_filter.show()

    def show_cat(self):
        self.hide()
        cat = Cat(self.signal_manager, parent=self)
        cat_filter = Cat_Filter(parent=self, child=cat)
        cat_filter.show()
    
    def show_pet(self):
        pet_filter = Pet_Filter(parent=self)
        self.hide()
        pet_filter.show()

    def show_dog_details(self):
        details = Dog_Detail1(parent=self)
        self.hide()
        details.show()
