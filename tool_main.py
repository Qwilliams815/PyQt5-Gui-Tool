import sys
import os
import json
# import uuid
from tool import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSettings

# ALL APPS DUMP
apps = set()
#profiles = set()

# CREATING A SAVE FILE FOR THE ADDED APPS
if not os.path.isfile('save.json'):
    open("save.json", "a+")


#if not os.path.isfile('save.txt'):
#    mem = open('save.txt', 'w+')

#with open('save.txt', 'r') as f:
#    for application in apps:
#        f.write(application + ',')


try:
    with open('save.json') as infile:
        profiles = json.load(infile)
        keys_list = []
        for key in profiles:
            keys_list.append(key)
        print("Available profiles: ", keys_list)
except:
    print('No Current Profiles')
    profiles = {}


# CONNECTING TO THE ORIGINAL UI.PY
class tool_window(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
        self.setupUi(self)
        #self.setStyleSheet("background-color: grey;")

        # lOADS SAVED PREVIOUSLY ADDED APPS
        for key in profiles:
            self.new_tab = qtw.QWidget()
            self.new_tab.setObjectName(f"{key}")
            self.tabWidget.addTab(self.new_tab, key)
            self.newTab_listWidget = qtw.QListWidget(self.new_tab)
            self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
            

            #list_name = f"{key}_list"
            #self.tab_listWidget = qtw.QListWidget(self.tabWidget)
            #QListWidget.setObjectName(self, list_name)
            #self.list_name = qtw.QListWidget(self.new_tab)
            #self.list_name.setGeometry(qtc.QRect(20, 10, 281, 441))

            #for app in profiles[key]:
            #    self.list_name.addItem(app)
            
        
        # PROFILE/TABS
        self.proButton.clicked.connect(self.add_tab)
        self.proNameEdit.returnPressed.connect(self.add_tab)


        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)

        # EMITS THE INDEX OF WHICH TAB IS REQUESTING CLOSURE
        self.tabWidget.tabCloseRequested.connect(self.remove_tab)
        

        # APPLICATIONS/LISTS
        self.appButton.clicked.connect(self.add_app)

        self.current_tab = self.tabWidget.currentWidget()
        #self.current_list = qtw.QListWidget(self.current_tab) #Creates listwidget on tab1
        
        # LAUNCH BUTTON
        #self.launchButton.clicked.connect(self.launch)
        self.launchButton.clicked.connect(self.test)
        



        #self.proButton.clicked.connect(self.add_profile)
        #self.new_tab.setObjectName("new_tab")
        #self.new_tab = qtw.QWidget()

    # Put all Functions(Methods) Here:

    def add_tab(self):

        # PROFILE NAME
        proName = self.proNameEdit.text()

        #profiles.add(proName)
        #print(profiles)
        #tab_id = proName + str(uuid.uuid4())
        #print(tab_id)

        # EMPTY PROFILE NAME CHECKER
        if proName == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Error: Profile name cannot be blank.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

        # PRE-EXISTING PROFILE CHECKER
        elif proName in profiles:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Error: Sorry, that profile already exists.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            #proName = self.proNameEdit.text()
            self.proNameEdit.clear()


        else:
            self.new_tab = qtw.QWidget()
            #self.new_tab.setObjectName("new_tab")
            self.tabWidget.addTab(self.new_tab, f"{proName}")
            self.proNameEdit.clear()
            profiles[proName] = []
            with open('save.json', 'w') as outfile:
                json.dump(profiles, outfile)
            # CREATES LISTWIDGET WITHIN TAB
            #self.newTab_listWidget = qtw.QListWidget(self.current_tab)
            #self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
            self.newTab_listWidget = qtw.QListWidget(self.new_tab)
            self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
            #self.newTab_listWidget.setObjectName(f"{proName}_listWidget")
            #print(self.f"{proName}_listWidget")
            


    def remove_tab(self, index):
        # print("close_handler called, index = %s" % index)
        self.tabWidget.removeTab(index)

        #TODO: Also delete json data of profile.

    def add_app(self):
        #self.current_tab = self.tabWidget.setCurrentWidget(self.tab_2)

        #if os.path.isfile('save.txt'):
        
        # Returns tuple: (filename, file type specifications)
        fileName = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'executables (*.exe)')
        

        #for profile in profiles:
        #    if profile == self.tabWidget.tabText(self.tabWidget.currentIndex()):
        #        pass

        # DUPLICATE FILE QUALIFIER
    #if fileName[0] not in apps:
        #apps.add(fileName[0])
        current_tab = self.tabWidget.tabText(self.tabWidget.currentIndex())
        profiles[current_tab].append(fileName[0])
        print(profiles)
        with open('save.json', 'w') as outfile:
            json.dump(profiles, outfile)
        # self.seperate_listWidget.addItem(fileName[0])
        
        #self.current_list.addItem("hello")
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
        
        #print(self.tabWidget.indexOf(self.tabWidget.currentWidget()))
        #print(self.tabWidget.currentWidget())

        #print(type(self.tabWidget))
        #print(type(self.tab))
        #print(type(self.tab1_listWidget))
        print(self.tabWidget.findChildren(self.tab, "tab"))



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    win = tool_window()


    win.show()


    app.exec_()