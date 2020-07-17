import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Combo Box")
        self.setGeometry(350, 350, 350, 350)
        self.UI()

    def UI(self):
        self.combo= QComboBox(self)
        self.combo.move(150, 100)
        button= QPushButton("save",self)
        button.move(150, 130)
        button.clicked.connect(self.getValue)
        self.combo.addItem("Python")
        self.combo.addItems(["c","cpp","c#","java","php"])
        list1=["pearl","julia","javascript"]
        for name in list1:
            self.combo.addItem(name)
        for number in range(10):
            self.combo.addItem(str(number))


        self.show()
    def getValue(self):
        value= self.combo.currentText()
        print(value)


def main():
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
     main()
