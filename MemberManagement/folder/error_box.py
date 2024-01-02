'''raise this error box when any error occurs'''
from PyQt6.QtWidgets import QMessageBox
class MessageBox(QMessageBox):
    '''create the meessage box'''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lỗi")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setStyleSheet("background-color: #FFCCCD; color: #132742")
