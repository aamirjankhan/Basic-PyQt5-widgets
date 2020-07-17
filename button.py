import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Buttons")
        self.setGeometry(500 , 250 , 300 , 300)
        self.UI()


    def UI(self):
        self.text=QLabel("My Text",self)
        enterButton=QPushButton("Enter",self)
        exitButton=QPushButton("Exit",self)
        exitButton.resize(100,22.5)
        self.text.move(110,50)
        enterButton.move(100,80)
        exitButton.move(200,80)

        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()
    def enterFunc(self):
        self.text.setText("You Clicked Enter")
        self.text.resize(150,20)
    def exitFunc(self):
        self.text.setText("You Clicked Exit")
        self.text.resize(150,20)

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()
