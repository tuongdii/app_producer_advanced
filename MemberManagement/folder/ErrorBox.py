from PyQt6.QtWidgets import QMainWindow, QMessageBox




class MessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lỗi")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setStyleSheet("background-color: #FFCCCD; color: #132742")