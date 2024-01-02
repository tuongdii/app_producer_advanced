from PyQt6 import uic, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QMessageBox
from folder.main_window import mainEmpty


class JoinTeam(QtWidgets.QDialog):
    def __init__(self, parent: QWidget):
        super().__init__()
        uic.loadUi("gui/joinTeam.ui", self)

        self.btnJoin.clicked.connect(self.checkCode)
        self.parent_widget = parent

    def checkCode(self):
        # Lấy mã code từ người dùng
        code = self.txtCode.text()
        msg_box = QMessageBox()
        # Kiểm tra mã code có được nhập hay không
        if not code:
            msg_box.setText("Vui lòng nhập mã code để tham gia team!")
            msg_box.exec()
            return

        # Kiểm tra mã code và thực hiện hành động tương ứng
        if code == "MindX":
            # Nếu mã code chính xác, chuyển sang giao diện chính (Main)
            self.parent_widget.signal_manager.join_successful.emit(
                self.parent_widget.username
            )
            self.close()
        else:
            # Nếu mã code không đúng, hiển thị thông báo lỗi
            msg_box.setText("Không tìm thấy team!")
            msg_box.exec()
            return


class RegisterOption(QtWidgets.QMainWindow):
    def __init__(self, signal_manager):
        super().__init__()
        uic.loadUi("gui/registerOption.ui", self)
        self.signal_manager = signal_manager
        self.username = ""
        self.join_team = JoinTeam(self)
        self.create_team = Create()

        # Bắt sự kiện khi người dùng nhấn vào text và icon để tham gia 1 team
        self.btn_join.clicked.connect(self.on_join_clicked)
        self.btnLogo_join.clicked.connect(self.on_join_clicked)

        # Bắt sự kiện khi người dùng nhấn vào text và icon để tạo 1 team mới
        self.btn_create.clicked.connect(self.on_create_clicked)
        self.btnLogo_create.clicked.connect(self.on_create_clicked)

    def show_window(self, username):
        self.username = username
        self.show()

    def on_join_clicked(self):
        self.join_team.show()
        self.close()

    def on_create_clicked(self):
        self.create_team.show()
        self.close()


class Create(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/create.ui", self)

        self.main_empty = mainEmpty()
        self.btnBack.clicked.connect(self.close)
        self.btnCreate.clicked.connect(self.checkCreate)

    def checkCreate(self):
        '''nhập tên team mới'''
        name = self.txtName.text()
        msg_box = QMessageBox()

        if not name:
            msg_box.setText("Vui lòng nhập tên team!")
            msg_box.exec()
            return

        self.main_empty.user_img.setPixmap(QtGui.QPixmap("img/user.png"))
        self.main_empty.lbName.setText(name)
        self.main_empty.lbWelcome.setText("Welcome to " + name + "'s team")
        self.main_empty.show()

        self.close()

