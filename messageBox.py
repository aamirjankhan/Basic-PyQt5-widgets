import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
font = QFont("Times",12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Message Box")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        button = QPushButton("Click me!!!", self)
        button2 = QPushButton("Click me!!!", self)
        button.setFont(font)
        button2.setFont(font)
        button.move(200, 150)
        button2.move(300, 150)
        button.clicked.connect(self.messageBox)
        button2.clicked.connect(self.messageBox1)
        self.show()
    def messageBox(self):

        mbox=QMessageBox()
        mbox.information(self, "Information", "You logged out!!!")
    def messageBox1(self):
        mbox=QMessageBox.question(self, "Warning!!!", "Are you sure to exit?",\
                                  QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel\
                                  ,QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
        elif mbox == QMessageBox.No:
            print("you clicked \"NO\" button")
def main():
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
     main()
