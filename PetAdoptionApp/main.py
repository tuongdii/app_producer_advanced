import sys

from PyQt6.QtWidgets import QApplication

from widget.login import Login, Register
from widget.main_window import MainWindow, SignalManager


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Tạo đối tượng quản lý tín hiệu
    signal_manager = SignalManager()

    # Tạo các đối tượng tương ứng với các trang giao diện
    loginPage = Login(signal_manager)
    registerPage = Register(signal_manager)
    mainPage = MainWindow(signal_manager)
    
    # Kết nối tín hiệu với chỗ giữ
    signal_manager.login_true.connect(mainPage.on_login_successful)
    signal_manager.register_true.connect(mainPage.on_register_successful)
    signal_manager.show_register_signal.connect(registerPage.show)
    signal_manager.show_login_signal.connect(loginPage.show)
    
    # Hiển thị trang Login đầu tiên
    loginPage.show()
    app.exec()
