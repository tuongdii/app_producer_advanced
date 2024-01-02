"""main program"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import pyqtSignal
from folder.login import Login, Register
from folder.main_window import MainWindow
from folder.team import RegisterOption


class SignalManager(QWidget):
    """define signals"""

    login_true = pyqtSignal(str)
    register_true = pyqtSignal(str)
    show_register_signal = pyqtSignal()
    show_login_signal = pyqtSignal()
    show_detail_signal = pyqtSignal()
    show_joinTeam = pyqtSignal(str)
    join_successful = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    """ Tạo đối tượng quản lý tín hiệu"""
    signal_manager = SignalManager()

    """ Tạo các đối tượng tương ứng với các trang giao diện"""
    loginPage = Login(signal_manager)
    registerPage = Register(signal_manager)
    mainPage = MainWindow(signal_manager)
    teamPage = RegisterOption(signal_manager)

    """Kết nối tín hiệu với chỗ giữ"""
    signal_manager.login_true.connect(mainPage.on_login_successful)
    signal_manager.register_true.connect(mainPage.on_register_successful)
    signal_manager.show_register_signal.connect(registerPage.show)
    signal_manager.show_login_signal.connect(loginPage.show)
    signal_manager.show_joinTeam.connect(teamPage.show_window)
    signal_manager.join_successful.connect(mainPage.on_join_successful)

    loginPage.show()
    sys.exit(app.exec())
