import sys
from PyQt5.QtWidgets import *

class Window(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar")
        self.show()

app = QApplication(sys.argv)
window = Window()
app.exec_()