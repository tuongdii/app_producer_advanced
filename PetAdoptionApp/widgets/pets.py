from PyQt6 import uic
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow


# Lớp chứa giao diện danh sách Dog
class Dog(QMainWindow):
    UI_LOCATION = "gui/dog.ui"
    def __init__(self, signal_manager, parent=None):
        super().__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        self.signal_manager = signal_manager
        self.parent = parent
        
        self.icon_state_list = [False] * 6  # Ban đầu, tất cả các icon đều chưa được chọn
        self.heart_buttons = [
            self.ui.heart1,
            self.ui.heart2,
            self.ui.heart3,
            self.ui.heart4,
            self.ui.heart5,
            self.ui.heart6]

        for button in self.heart_buttons:
            button.clicked.connect(self.toggle_heart_icon)
        
        self.ui.btn_back.clicked.connect(self.back)
        self.ui.btn_dog1.clicked.connect(self.show_detail)
        # self.ui.btn_name_dog1.clicked.connect(self.showDetail)

    def toggle_heart_icon(self):
        button = self.sender()  # Lấy thông tin về nút gửi sự kiện
        if button in self.heart_buttons:  # Kiểm tra nút có trong danh sách
            button_index = self.heart_buttons.index(button)
            if not self.icon_state_list[button_index]:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/icons8-heart-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = True
            else:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/tyn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = False
                
    def back(self):
        self.parent.show()
        self.close()
        
    def show_detail(self):
        self.signal_manager.show_detail_signal.emit()
        self.close()
        

# Lớp chứa giao diện danh sách Cat
class Cat(QMainWindow):
    UI_LOCATION = "gui/cat.ui"
    def __init__(self, signal_manager, parent=None):
        super().__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self) 
        self.signal_manager = signal_manager
        self.parent = parent
        
        self.icon_state_list = [False] * 6  # Ban đầu, tất cả các icon đều chưa được chọn
        self.heart_buttons = [
                                self.ui.heart1,
                                self.ui.heart2,
                                self.ui.heart3,
                                self.ui.heart4,
                                self.ui.heart5,
                                self.ui.heart6
                            ]

        for button in self.heart_buttons:
            button.clicked.connect(self.toggle_heart_icon)
        self.ui.btn_back.clicked.connect(self.back)
        
    #Viết hàm để thay đổi hình dạng trái tim khi người dùng click vào
    def toggle_heart_icon(self):
        button = self.sender()  # Lấy thông tin về nút gửi sự kiện
        if button in self.heart_buttons:  # Kiểm tra nút có trong danh sách
            button_index = self.heart_buttons.index(button)
            #Kiểm tra nếu thú cưng chưa được thêm vào danh sách yêu thích khi bấm vào icon trái tym sẽ full màu
            if not self.icon_state_list[button_index]:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/icons8-heart-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = True
            ##Kiểm tra nếu thú cưng đã được thêm vào danh sách yêu thích khi bấm vào icon trái tym sẽ không full mày
            else:
                iconheart = QtGui.QIcon()
                iconheart.addPixmap(QtGui.QPixmap("img/tyn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                button.setIcon(iconheart)
                self.icon_state_list[button_index] = False
    
    def back(self):
        self.parent.show()
        self.close()


# Lớp chứa giao diện chi tiết Dog
class Dog_Detail(QMainWindow):
    UI_LOCATION = "gui/dog_detail.ui"
    def __init__(self, parent):
        super(Dog_Detail, self).__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        
        self.parent = parent
        #Chọn trờ về trang main 
        self.ui.btn_back.clicked.connect(self.close)
        
    def close(self):
        self.close()
        self.parent.show()
        
# Lớp chứa giao diện chi tiết Dog 1
class Dog_Detail1(QMainWindow):
    UI_LOCATION = "gui/dog_detail1.ui"
    def __init__(self, parent=None):
        super(Dog_Detail1, self).__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        self.parent = parent

        #Chọn trờ về trang main 
        self.ui.btn_back.clicked.connect(self.back)
        
    def back(self):
        self.close()  
        self.parent.show()
