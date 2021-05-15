import sys
import os
import json
from tool import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QTabWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSettings


# CREATING A .JSON SAVE FILE FOR THE ADDED PROFILES / APPS
if not os.path.isfile('save.json'):
    open("save.json", "a+")

# LOADS .JSON DATA INTO THE 'PROFILES' VARIABLE
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


        self.setupUi(self)
        #self.setStyleSheet("background-color: grey;")

        if profiles == {}:
            #
            self.tut_tab = qtw.QWidget()
            self.tabWidget.addTab(self.tut_tab, "Get Started")

            # CREATES LISTWIDGET WITHIN TAB
            self.newTab_listWidget = qtw.QListWidget(self.tut_tab)
            self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
            self.newTab_listWidget.addItem("Hello!")
            self.newTab_listWidget.addItem("Welcome to my BootUp Tool 1.0")
            self.newTab_listWidget.addItem("To get started,")
            self.newTab_listWidget.addItem("- Enter a profile name")
            self.newTab_listWidget.addItem('- Hit Enter or "Add Profile"')
            self.newTab_listWidget.addItem("- Select any apps you wish to boot")
            self.newTab_listWidget.addItem("- Rinse and repeat!")
            
            #


        # lOADS ANY PREVIOUSLY SAVED ADDED PROFILES / APPS
        i = 0
        for key in profiles:

            # CREATES A TAB FOR EACH PROFILE
            self.new_tab = qtw.QWidget()
            self.tabWidget.addTab(self.new_tab, key)

            # CREATES A LIST WIDGET FOR EACH TAB
            self.newTab_listWidget = qtw.QListWidget(self.new_tab)
            self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))

            # APPENDS ANY APPS TO SAID TAB'S LIST WIDGET
            for item in profiles[key]:
                self.newTab_listWidget.addItem(item)

            # SETS NEW OBJECT NAMES FOR ITERATION PURPOSES
            self.new_tab.setObjectName(f"{key}")
            self.newTab_listWidget.setObjectName(f"newTab_listWidget{i}")

            i += 1
            
        
        # PROFILE/TABS BUTTON FUNC / SPECS
        self.proButton.clicked.connect(self.add_tab)
        self.proNameEdit.returnPressed.connect(self.add_tab)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(False)

        # EMITS THE INDEX OF WHICH TAB IS REQUESTING CLOSURE
        self.tabWidget.tabCloseRequested.connect(self.remove_tab)
        

        # APPLICATIONS/LISTS BUTTON FUNC / SPECS
        self.appButton.clicked.connect(self.add_app)

        
        # LAUNCH BUTTON FUNC
        self.launchButton.clicked.connect(self.launch)


    # BUTTON FUNCTIONS / METHODS

    def add_tab(self):

        # PROFILE NAME
        proName = self.proNameEdit.text()

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
            self.proNameEdit.clear()

        else: 

    
            # CREATES NEW TAB
            self.new_tab = qtw.QWidget()
            self.tabWidget.addTab(self.new_tab, f"{proName}")
            self.proNameEdit.clear()

            # CREATES LISTWIDGET WITHIN TAB
            self.newTab_listWidget = qtw.QListWidget(self.new_tab)
            self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
            #self.newTab_listWidget.addItem("HELLO")


            try:
                if self.tabWidget.indexOf(self.tut_tab) == 0:
                    self.tabWidget.removeTab(0)
            except:
                pass
            
            i = self.tabWidget.indexOf(self.new_tab)
            print(i)

            # SAVES TAB WITH EMPTY LIST AS KEY VALUE PAIR IN .JSON SAVE FILE
            profiles[proName] = []
            with open('save.json', 'w') as outfile:
                json.dump(profiles, outfile)


            # SETS NEW OBJECT NAMES FOR ITERATION PURPOSES
            self.new_tab.setObjectName(f"{proName}")
            self.newTab_listWidget.setObjectName(f"newTab_listWidget{i}")
        

    def add_app(self):
        
        # LAUNCHES FILE EXPLORER, RETURNS TUPLE: (FILENAME, FILE TYPE SPECIFICATIONS)
        fileName = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'executables (*.exe)')

        # GATHERS CURRENT TAB/LIST FOR APPENDING THE APP
        current_tab_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
        print("Current tab Name: ", current_tab_name)
        current_tab_index = self.tabWidget.currentIndex()
        print("Current tab index: ", current_tab_index)
        self.current_list = self.tabWidget.findChild(QListWidget, f"newTab_listWidget{current_tab_index}")
        print(self.current_list)


        # APPENDS APP TO TAB LIST AND .JSON SAVE FILE
        profiles[current_tab_name].append(fileName[0])
        self.current_list.addItem(fileName[0])
        print("Added to List")

        with open('save.json', 'w') as outfile:
            json.dump(profiles, outfile)


    def remove_tab(self, index):

        self.removed_tab = self.tabWidget.tabText(index)
        self.removed_tab_list = self.tabWidget.findChild(QListWidget, f"newTab_listWidget{index}")
        del profiles[self.removed_tab]

        # REMOVES TAB/LISTWIDGET FROM GUI
        self.tabWidget.removeTab(index)
        self.removed_tab_list.setParent(None)

        i = 0
        for self.list in self.tabWidget.findChildren(QListWidget):
            self.list.setObjectName(f"newTab_listWidget{i}")
            i += 1

        with open('save.json', 'w') as outfile:
            json.dump(profiles, outfile)


    def launch(self):

        current_tab_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
        for app in profiles[current_tab_name]:
            os.startfile(app)

    def test(self):
        pass

            



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    win = tool_window()
    win.show()
    app.exec_()