import sys
import os
from tool import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QFileDialog

apps = set()

if not os.path.isfile('save.txt'):
    mem = open('save.txt', 'w+')

        

#with open('save.txt', 'r') as f:
#    for application in apps:
#        f.write(application + ',')



#Connecting to the original ui.py
class tool_window(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
        self.setupUi(self)

        #lOADS SAVED PREVIOUSLY ADDED APPS
        with open('save.txt', 'r') as f:
            tempApps = f.read()
            tempApps = tempApps.split(',')
            for app in tempApps:
                apps.add(app)
                self.seperate_listWidget.addItem(app)

        self.proButton.clicked.connect(self.add_tab)

        self.appButton.clicked.connect(self.add_app)
        
        self.launchButton.clicked.connect(self.launch)
        



       #self.proButton.clicked.connect(self.add_profile)
        #self.new_tab.setObjectName("new_tab")
        #self.new_tab = qtw.QWidget()

    # Put all Functions(Methods) Here:

    def add_tab(self):
        self.new_tab = qtw.QWidget()
        #self.new_tab.setObjectName("new_tab")
        proName = self.proNameEdit.text()
        self.tabWidget.addTab(self.new_tab, f"{proName}")
        self.proNameEdit.clear()

    def add_app(self):

        #if os.path.isfile('save.txt'):
        
                

        fileName = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'executables (*.exe)')

        # DUPLICATE FILE QUALIFIER
        if fileName[0] not in apps:
            apps.add(fileName[0])
            self.seperate_listWidget.addItem(fileName[0])
            with open('save.txt', 'w') as f:
                for application in apps:
                    f.write(application + ',')
        print(apps)

    def launch(self):
        for app in apps:
            os.startfile(app)



        


    def test_message(self):
        print("Hello there")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    win = tool_window()


    win.show()


    app.exec_()