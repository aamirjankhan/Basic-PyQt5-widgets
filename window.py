import sys
from PyQt5.QtWidgets import * # * means we have imported everything from QTWidgets

class Window(QWidget): #class for our window and we have inherited the libraries form class QWidgets
    def __init__(self): #constructor for class Window
        super().__init__() #constructor for super class QWidgets
        self.setGeometry(500 , 250 , 300 , 450)
        #first argument indicates 50 pixels from the x axis
        #second argument indicated 50 pixels from the y axis
        #third argument indicates 300 pixels of length on the x axis
        #fourth argument indicates 450 pixels of length on the y axis
        self.setWindowTitle("This is our window title") #setting window title
        self.show() #so that we can view our created window
App=QApplication(sys.argv)
window=Window() #instance for class Window
sys.exit(App.exec_())
