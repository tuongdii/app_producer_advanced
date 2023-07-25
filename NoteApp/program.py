from PyQt6 import QtWidgets as qtw
from PyQt6 import uic
import sys 
import re

page = 1
class NoteApp(qtw.QDialog):
    def __init__(self):
        super(NoteApp, self).__init__()
        uic.loadUi("gui/noteApps.ui", self)
        
        self.btn_edit1.clicked.connect(self.updatePage)
        self.btn_edit1.clicked.connect(self.edit)
        
        self.btn_edit2.clicked.connect(self.updatePage)
        self.btn_edit2.clicked.connect(self.edit)
        
        self.btn_edit3.clicked.connect(self.updatePage)
        self.btn_edit3.clicked.connect(self.edit)
        
        self.btn_edit4.clicked.connect(self.updatePage)
        self.btn_edit4.clicked.connect(self.edit)

    
    def edit(self):
        self.detail = Detail()
        self.detail.show()
        
    def updatePage(self):
        global page
        button_name = self.sender().objectName()
        page_number = re.search(r'\d+', button_name)
        if page_number:
            page = int(page_number.group())
    
class Detail(qtw.QDialog):
    def __init__(self):
        super(Detail, self).__init__()
        pageName = "gui/details" + str(page) + ".ui"
        uic.loadUi(pageName, self)
        self.btn_close.clicked.connect(lambda:self.close())
    
        
                            
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = NoteApp()
    window.show()
    app.exec()