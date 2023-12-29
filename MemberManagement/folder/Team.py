from PyQt6 import uic,QtGui,QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Login import Register



from folder.mainWindow import MainWindow
class JoinTeam(QMessageBox.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/joinTeam.ui", self)
    
        self.btnJoin.clicked.connect(self.checkCode)
        
        
    def checkCode(self):
        # Lấy mã code từ người dùng
        code = self.txtCode.text()
        msg_box=QMessageBox()
        # Kiểm tra mã code có được nhập hay không
        if not code: 
            msg_box.setText("Vui lòng nhập mã code để tham gia team!")
            msg_box.exec()
            return
        
        # Kiểm tra mã code và thực hiện hành động tương ứng
        if code == "MindX":
            main=MainWindow()
            # Nếu mã code chính xác, chuyển sang giao diện chính (Main)
            main.lblUser.setPixmap(QtGui.QPixmap("img/user.png"))
            main.lbUsername.setText(registerWindow.username)
            main.show()
            self.close()
            registerOption.hide()
        else:
            # Nếu mã code không đúng, hiển thị thông báo lỗi
            msg_box.setText("Không tìm thấy team!")
            msg_box.exec()
            return
class RegisterOption(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/registerOption.ui", self)
        
        self.joinTeam = JoinTeam()
        self.create = Create()
        
        #Bắt sự kiện khi người dùng nhấn vào text và icon để tham gia 1 team
        self.btn_join.clicked.connect(self.joinTeam.show)
        self.btnLogo_join.clicked.connect(self.joinTeam.show)
        
        #Bắt sự kiện khi người dùng nhấn vào text và icon để tạo 1 team mới
        self.btn_create.clicked.connect(self.create.show)
        self.btnLogo_create.clicked.connect(self.create.show)
class MainEmpty(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/mainEmpty.ui", self)    

class Create(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/create.ui", self)
        
        self.mainEmpty = MainEmpty()
        self.btnBack.clicked.connect(self.close)
        self.btnCreate.clicked.connect(self.checkCreate)
    
    def checkCreate(self):
        # Lấy thông tin tên từ người dùng
        name = self.txtName.text()
        msg_box = QMessageBox()
        # Kiểm tra tên có được nhập hay không
        if not name:
            msg_box.setText("Vui lòng nhập tên team!")
            msg_box.exec()
            return
        
        # Hiển thị thông báo chào mừng và chuyển sang giao diện chính (MainEmpty)
        self.mainEmpty.lblUser.setPixmap(QtGui.QPixmap("img/user.png"))
        self.mainEmpty.lbName.setText(registerWindow.username)
        self.mainEmpty.lbWelcome.setText("Welcome to " + name + "'s team")
        self.mainEmpty.show()
        self.close()
        registerOption.hide()

registerOption = RegisterOption()
registerWindow = Register()