import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using LineEdit")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please enter your name:")
        self.nameTextBox.resize(250, 20)
        self.nameTextBox.move(120 , 50)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText("Please enter your password:")
        self.passTextBox.resize(150, 20)
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120 , 80)
        button= QPushButton("check",self)
        button.clicked.connect(self.showData)
        button.move(120, 110)
        self.lable=QLabel("Data will be shown in the title...",self)
        self.lable.move(120, 140)
        self.show()
    def showData(self):
        name=self.nameTextBox.text()
        password=self.passTextBox.text()
        self.setWindowTitle("your name is: "+name+" your password is: "+password)



def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
