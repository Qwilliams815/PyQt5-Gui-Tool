from tool import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

#Connecting to the original ui.py
class tool_window(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.setupUi(self)


        self.proButton.clicked.connect(self.add_profile)
        self.tab3 = qtw.QWidget()

    #Put all Functions(Methods) Here:
    def add_profile(self):
        self.addTab(self.tab3, "tab 3")
        print("ok")



if __name__ == '__main__':
    app = qtw.QApplication([])

    win = tool_window()
    win.show()

    app.exec_()