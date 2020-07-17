import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
font = QFont("Times",12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Text Editor")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.editor= QTextEdit(self)
        self.editor.move(150,80)
        button=QPushButton("Send",self)
        button.move(330,280)
        button.clicked.connect(self.getValue)
        self.editor.setAcceptRichText(True)

        self.show()
    def getValue(self):
        text=self.editor.toPlainText()
        print(text)



def main():
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
     main()
