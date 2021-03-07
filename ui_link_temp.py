# Template used to link edits to the original ui file

#from - the original ui.py file - import - whatever window scheme you selected in designer (widget, mainwindow, etc)"
from tool import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

#Connecting to the original ui.py, again use whatever window scheme you selected as an inheritance.
class tool_window(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.setupUi(self)


    #Put all Functions(Methods) Here:
    def function(self):
        pass


if __name__ == '__main__':
    app = qtw.QApplication([])

    win = tool_window()
    win.show()

    app.exec_()