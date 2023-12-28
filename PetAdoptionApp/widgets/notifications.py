from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic


# Lớp chứa giao diện thông báo không tìm thấy
class NotFound(QMainWindow):
    UI_LOCATION = "gui/notFound.ui"
    def __init__(self, parent=None):
        super(NotFound, self).__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        self.parent = parent
        
        self.ui.btn_back.clicked.connect(self.back)
        
    def back(self):
        self.close()
        self.parent.show()

class MessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lỗi")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setStyleSheet("background-color: #F8F2EC; color: #356a9c")