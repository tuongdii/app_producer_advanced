# from PyQt6 import QtWidgets, QtGui, QtCore
# from PyQt6.QtWidgets import QMessageBox
# from PyQt6 import uic
# import re

# from folder.main_window import MainWindow

# class Login(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("gui/login.ui", self)
        
#         #Bắt sự kiện click chuột nào nút login
#         self.btnLogin.clicked.connect(self.check_login)
#         #Bắt sự kiện click chuột nào liên kết register
#         self.btn_register.clicked.connect(self.showRegister)
      
#     def check_login(self):
#         # Lấy thông tin email và mật khẩu từ người dùng
#         email = self.txtEmail.text()
#         password = self.txtPassword.text()
        
#         # Kiểm tra email và mật khẩu có được nhập hay không
#         if not email: 
#             msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
#             msg_box.exec()
#             return
#         if not password:
#             msg_box.setText("Vui lòng nhập mật khẩu!")
#             msg_box.exec()
#             return
        
#         # Kiểm tra email và mật khẩu có khớp với tài khoản admin hay không
#         if email == "admin@example.com" and password == "admin":
#             # Nếu đăng nhập thành công, chuyển sang giao diện chính (Main)
#             self.close()
#             main_window.show()  
#         else:
#             # Nếu đăng nhập không thành công, hiển thị thông báo lỗi
#             msg_box.setText("Email hoặc mật khẩu không đúng!")
#             msg_box.exec()
    
#     def showRegister(self):
#         # Hiển thị giao diện đăng ký (Register)
#         registerWindow.show()
#         self.close()


# class Register(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("gui/register.ui", self)
#         self.username = ""
        
#         #Bắt sự kiện 
#         self.btnRegister.clicked.connect(self.Register)
#         self.btn_Login.clicked.connect(self.showLoginPage)
    
#     def Register(self):
#         # Lấy thông tin email, username và mật khẩu từ người dùng
#         email = self.txtEmail.text()
#         self.username = self.txtUsername.text()
#         password = self.txtPassword.text()
        
#         # Kiểm tra các trường thông tin có được nhập hay không
#         if not email: 
#             msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
#             msg_box.exec()
#             return
#         if not self.username:
#             msg_box.setText("Vui lòng nhập username!")
#             msg_box.exec()
#             return
#         if not password:
#             msg_box.setText("Vui lòng nhập mật khẩu!")
#             msg_box.exec()
#             return
#         if not self.checkBox.isChecked():
#             msg_box.setText("Vui lòng đọc và đồng ý các điều khoản của MemberHub!")
#             msg_box.exec()
#             return
        
#         # Đóng giao diện đăng ký và hiển thị giao diện lựa chọn đăng ký (registerOption)
#         self.close()
#         registerOption.show()
    
#     def showLoginPage(self):
#         # Hiển thị giao diện đăng nhập (loginWindow)
#         loginWindow.show()
#         self.close()

    
# class RegisterOption(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("gui/registerOption.ui", self)
        
#         self.joinTeam = JoinTeam()
#         self.create = Create()
        
#         #Bắt sự kiện khi người dùng nhấn vào text và icon để tham gia 1 team
#         self.btn_join.clicked.connect(self.joinTeam.show)
#         self.btnLogo_join.clicked.connect(self.joinTeam.show)
        
#         #Bắt sự kiện khi người dùng nhấn vào text và icon để tạo 1 team mới
#         self.btn_create.clicked.connect(self.create.show)
#         self.btnLogo_create.clicked.connect(self.create.show)

# class Create(QtWidgets.QDialog):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("gui/create.ui", self)
        
#         self.mainEmpty = MainEmpty()
#         self.btnBack.clicked.connect(self.close)
#         self.btnCreate.clicked.connect(self.checkCreate)
    
#     def checkCreate(self):
#         # Lấy thông tin tên từ người dùng
#         name = self.txtName.text()
        
#         # Kiểm tra tên có được nhập hay không
#         if not name:
#             msg_box.setText("Vui lòng nhập tên team!")
#             msg_box.exec()
#             return
        
#         # Hiển thị thông báo chào mừng và chuyển sang giao diện chính (MainEmpty)
#         self.mainEmpty.user_img.setPixmap(QtGui.QPixmap("img/user.png"))
#         self.mainEmpty.lbName.setText(registerWindow.username)
#         self.mainEmpty.lbWelcome.setText("Welcome to " + name + "'s team")
#         self.mainEmpty.show()
#         self.close()
#         registerOption.hide()

# class MainEmpty(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("gui/mainEmpty.ui", self)    


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     loginWindow = Login()
#     registerOption = RegisterOption()
#     main_window = MainWindow()
#     registerWindow = Register()
    
#     # Thiết lập hộp thoại thông báo lỗi
#     msg_box=QMessageBox()

#     loginWindow.show()
#     sys.exit(app.exec())
