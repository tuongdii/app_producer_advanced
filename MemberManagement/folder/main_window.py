from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6 import uic, QtGui
import re

class SignalManager(QWidget):
    login_true = pyqtSignal(str)
    register_true = pyqtSignal(str)
    show_register_signal = pyqtSignal()
    show_login_signal = pyqtSignal()
    show_detail_signal = pyqtSignal()
    show_joinTeam = pyqtSignal(str)
    join_successful = pyqtSignal(str)


class MainWindow(QMainWindow):
    def __init__(self, signal_manager:SignalManager):
        super().__init__()
        self.ui=uic.loadUi("gui/main.ui", self)
        self.signal_manager = signal_manager
       
        self.ui.btn_viewImg1.clicked.connect(self.view_details)
        self.ui.btn_view1.clicked.connect(self.view_details)
        self.ui.btn_view2.clicked.connect(self.view_details)
        self.ui.btn_view3.clicked.connect(self.view_details)
        self.ui.btn_view4.clicked.connect(self.view_details)
        self.ui.btn_view5.clicked.connect(self.view_details)
        self.ui.btn_view6.clicked.connect(self.view_details)       
        self.ui.btn_viewImg2.clicked.connect(self.view_details)
        self.ui.btn_viewImg3.clicked.connect(self.view_details)
        self.ui.btn_viewImg4.clicked.connect(self.view_details)
        self.ui.btn_viewImg5.clicked.connect(self.view_details)
        self.ui.btn_viewImg6.clicked.connect(self.view_details)

    def view_details(self):
        self.detail = Detail()
        self.detail.show()

    def on_login_successful(self, username):
        self.ui.user_name.setText(username)
        self.show()
    
    def on_register_successful(self, username):
        self.ui.user_name.setText(username)
        self.show()
    
    def on_join_successful(self, username):
        self.ui.user_img.setPixmap(QtGui.QPixmap("img/user.png"))
        self.ui.user_name.setText(username)
        self.show()


class Detail(QMainWindow):
        def __init__(self):
            super().__init__()
            page = 1
            button_name = self.sender().objectName()
            page_number = re.search(r'\d+', button_name)
            if page_number:
                page = int(page_number.group())

            pageName = "gui/details" + str(page) + ".ui"
            uic.loadUi(pageName, self)
            self.btn_back.clicked.connect(self.close)
