from PyQt6 import QtWidgets as qtw
from PyQt6 import uic
import sys 

page = 1
class Ranking(qtw.QMainWindow):
    def __init__(self):
        super(Ranking, self).__init__()
        uic.loadUi("leaderboard.ui", self)
    
                            
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Ranking()
    window.show()
    app.exec()