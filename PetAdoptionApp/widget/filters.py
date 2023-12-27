from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

from widget.notifications import NotFound


# Lớp chứa bộ lọc danh sách Dog
class Dog_Filter(QDialog):
    UI_LOCATION = "gui/dog_filter.ui"
    def __init__(self, parent=None, child=None):
        super().__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        self.parent = parent
        self.child = child
        
        self.ui.btn_back.clicked.connect(self.back)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_continue.clicked.connect(self.view_dogs)

    def view_dogs(self):
        self.close()
        self.parent.close()
        self.child.show()
    
    def back(self):
        self.close()
        self.parent.show()


# Lớp chứa bộ lọc danh sách Cat
class Cat_Filter(QDialog):
    UI_LOCATION = "gui/cat_filter.ui"
    def __init__(self, parent=None, child=None):
        super().__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self)
        self.parent = parent
        self.child = child
        
        self.ui.btn_back.clicked.connect(self.back)
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_continue.clicked.connect(self.view_cats)

    def view_cats(self):
        self.close()
        self.parent.close()
        self.child.show()

    def back(self):
        self.close()
        self.parent.show()

# Lớp chứa bộ lọc danh sách Pet
class Pet_Filter(QDialog):
    UI_LOCATION = "gui/animal_filter.ui"
    def __init__(self, parent=None):
        super().__init__()
        self.ui = uic.loadUi(self.UI_LOCATION, self)  
        self.parent = parent
        self.child = NotFound(self.parent)
        
        self.ui.btn_back.clicked.connect(self.back)  
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_rabbit.clicked.connect(self.showNotFound)
        self.ui.btn_rabbitName.clicked.connect(self.showNotFound)
        self.ui.btn_pig.clicked.connect(self.showNotFound)
        self.ui.btn_pigName.clicked.connect(self.showNotFound)
        self.ui.btn_bird.clicked.connect(self.showNotFound) 
        self.ui.btn_birdName.clicked.connect(self.showNotFound)  
        self.ui.btn_hamster.clicked.connect(self.showNotFound) 
        self.ui.btn_hamsterName.clicked.connect(self.showNotFound) 

    def showNotFound(self):
        self.close()
        self.child.show()
    
    def back(self):
        self.close()
        self.parent.show()
