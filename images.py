import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Buttons")
        self.setGeometry(500 , 250 , 300 , 300)
        self.UI()


    def UI(self):
        self.image= QLabel(self)
        self.image.setPixmap(QPixmap("images/pyLogo.png"))
        self.image.move(90, 50)
        self.removeButton= QPushButton("remove", self)
        self.removeButton.move(70, 180)
        self.removeButton.clicked.connect(self.removeImg)
        self.showButton= QPushButton("show", self)
        self.showButton.move(150, 180)
        self.showButton.clicked.connect(self.showImg)
        self.show()

    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()




def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()
