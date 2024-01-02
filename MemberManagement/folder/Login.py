from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from folder.error_box import MessageBox




class Login(QMainWindow):
    """ Lớp chứa giao diện đăng nhập"""
    def __init__(self, signal_manager):
        super().__init__()
        self.ui = uic.loadUi("gui/login.ui", self)
        self.signal_manager = signal_manager

        self.ui.btnLogin.clicked.connect(self.check_login)
        self.ui.btn_register.clicked.connect(self.show_register)
        self.msg_box = MessageBox()

    def check_login(self):
        """Lấy thông tin email và mật khẩu từ người dùng"""
        email = self.ui.txtEmail.text()
        password = self.ui.txtPassword.text()

        if not email:
            self.msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("Vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return

        if email == "admin" and password == "admin":
            self.emit_login_signal("admin")
            self.close()
        else:
            self.msg_box.setText("Email hoặc mật khẩu không đúng!")
            self.msg_box.exec()

    def show_register(self):
        self.signal_manager.show_register_signal.emit()
        self.close()

    def emit_login_signal(self, username):
        self.signal_manager.login_true.emit(username)


# Lớp chứa giao diện đăng ký
class Register(QMainWindow):
    def __init__(self, signal_manager):
        super().__init__()
        self.ui = uic.loadUi("gui/register.ui", self)
        self.signal_manager = signal_manager

        """ Bắt sự kiện click chuột vào nút đăng ký"""
        self.btnRegister.clicked.connect(self.register)

        self.btn_Login.clicked.connect(self.show_login)
        self.msg_box = MessageBox()

    def register(self):
        """Lấy thông tin email, username và mật khẩu từ người dùng"""
        name = self.ui.txtUsername.text()
        email = self.ui.txtEmail.text()
        password = self.ui.txtPassword.text()

        """ Kiểm tra các trường thông tin có được nhập hay không"""
        if not name:
            self.msg_box.setText("Vui lòng nhập username!")
            self.msg_box.exec()
            return
        if not email:
            self.msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("Vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        if not self.ui.checkBox.isChecked():
            self.msg_box.setText("Vui lòng đọc và đồng ý các điều khoản của MemberHub!")
            self.msg_box.exec()
            return

        self.emit_join_team_signal()
        self.close()

    def emit_register_signal(self):
        username = self.ui.txtUsername.text()
        self.signal_manager.register_true.emit(username)

    def emit_join_team_signal(self):
        username = self.ui.txtUsername.text()
        self.signal_manager.show_joinTeam.emit(username)
        self.close()

    def show_login(self):
        self.signal_manager.show_login_signal.emit()
        self.close()
