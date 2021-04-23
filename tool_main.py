import sys
import os
# import uuid
from tool import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSettings

apps = set()
profiles = set()

# CREATING A SAVE FILE FOR THE ADDED APPS
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
        #self.setStyleSheet("background-color: grey;")

        #lOADS SAVED PREVIOUSLY ADDED APPS
        
        with open('save.txt', 'r') as f:
            tempApps = f.read()
            tempApps = tempApps.split(',')
            for app in tempApps:
                apps.add(app)
                self.seperate_listWidget.addItem(app)
        
        # PROFILE/TABS
        self.proButton.clicked.connect(self.add_tab)
        self.proNameEdit.returnPressed.connect(self.add_tab)

        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)

        # Emits the index of which tab is requesting closure
        self.tabWidget.tabCloseRequested.connect(self.remove_tab)
        

        # APPLICATIONS/LISTS
        self.appButton.clicked.connect(self.add_app)

        self.current_tab = self.tabWidget.currentWidget()
        self.current_list = qtw.QListWidget(self.current_tab)
        
        # LAUNCH BUTTON
        #self.launchButton.clicked.connect(self.launch)
        self.launchButton.clicked.connect(self.test)
        



        #self.proButton.clicked.connect(self.add_profile)
        #self.new_tab.setObjectName("new_tab")
        #self.new_tab = qtw.QWidget()

    # Put all Functions(Methods) Here:

    def add_tab(self):
        proName = self.proNameEdit.text()
        profiles.add(proName)
        print(profiles)
        #tab_id = proName + str(uuid.uuid4())
        #print(tab_id)

        if proName != "": # EMPTY TAB NAME VALIDATER
            self.new_tab = qtw.QWidget()
            #self.new_tab.setObjectName("new_tab")
            self.tabWidget.addTab(self.new_tab, f"{proName}")
            self.proNameEdit.clear()

            #CREATES LISTWIDGET WITHIN TAB
            self.newTab_listWidget = qtw.QListWidget(self.current_tab)
            self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
            # self.newTab_listWidget = qtw.QListWidget(self.new_tab)
            # self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
            #self.newTab_listWidget.setObjectName(f"{proName}_listWidget")
            #print(self.f"{proName}_listWidget")

        else: # EMPTY TAB NAME ERROR POP-UP MSG
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Error: Profile name cannot be blank.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()


    def remove_tab(self, index):
        # print("close_handler called, index = %s" % index)
        self.tabWidget.removeTab(index)

    def add_app(self):
        #self.current_tab = self.tabWidget.setCurrentWidget(self.tab_2)
        
        
        

        #if os.path.isfile('save.txt'):
        
        # Returns tuple: (filename, file type specifications)
        fileName = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'executables (*.exe)')

        #for profile in profiles:
        #    if profile == self.tabWidget.tabText(self.tabWidget.currentIndex()):
        #        pass

        # DUPLICATE FILE QUALIFIER
        if fileName[0] not in apps:

            apps.add(fileName[0])
            #current_tab = self.tabWidget.tabText(self.tabWidget.currentIndex())

            # self.seperate_listWidget.addItem(fileName[0])
            for profile in profiles:
                pass
            
            self.current_list.addItem("hello")
            #self.qtw.QListWidget(self.self.tabWidget.currentWidget()).addItem('Hello')
            #$self.currentListWidget = self.tabWidget.tabText(self.tabWidget.currentIndex()) + "_listWidget"
            #$self.currentListWidget.addItem(fileName[0])


            # SAVING THE APP
            #with open('save.txt', 'w') as f:
            #    for application in apps:
            #        f.write(application + ',')

        #self.tabWidget.currentWidget.tab.tab1_listWidget.addItem(fileName[0])




        print(apps)

    def launch(self):
        for app in apps:
            os.startfile(app)


    def test(self):
        #print(self.tabWidget.tabText(self.tabWidget.currentIndex()))
        #print(self.tabWidget.currentIndex())
        #print(self.tabWidget.tabText(self.tabWidget.currentIndex()) + "_listWidget")
        #print(self.tabWidget.currentWidget.tab1_listWidget)

        #print([tab for tab in range(0, self.tabWidget.count()) if self.tabWidget.currentIndex() == tab])
        # 1 for tab in range(0, self.tabWidget.count()):
        # 1     if self.tabWidget.currentIndex() == tab:
        # 1         self.newTab_listWidget.addItem("Hello")
        # 1         print(self.tabWidget.currentIndex())
        #        self.tabWidget.count[tab]
        #print(self.findChildren(self.tabWidget))
        
        print(self.tabWidget.indexOf(self.tabWidget.currentWidget()))
        #print(self.tabWidget.currentWidget())



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    win = tool_window()


    win.show()


    app.exec_()