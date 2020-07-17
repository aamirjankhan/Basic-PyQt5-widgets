import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using lables")
        self.setGeometry(500 , 250 , 300 , 450)
        self.UI()

    def UI(self):
        text1=QLabel("Python GUI",self)
        text2=QLabel("Hello World",self)
        text1.move(0,0)
        text2.move(0,50)
        self.show()


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()

