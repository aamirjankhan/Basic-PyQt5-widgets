import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practice")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.Button1 = QPushButton("Cehck",self)
        self.Button1.clicked.connect(self.CheckFunc)
        self.Button1.move(120, 20)
        self.text= QLabel("Check",self)
        self.text.move(120, 110)
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please enter your name:")
        self.nameTextBox.resize(150, 20)
        self.nameTextBox.move(120 , 50)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText("Please enter your password:")
        self.passTextBox.resize(150, 20)
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120 , 80)
        self.show()
    def CheckFunc(self):
        if self.nameTextBox.Text() == "aamir.jankhan445@gmail.com" and self.passTextBox.text() == "!ciit12345":
            self.text.setText("correct")



def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
