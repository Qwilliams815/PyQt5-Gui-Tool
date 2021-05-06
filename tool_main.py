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
apps = []
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

        # lOADS SAVED PREVIOUSLY ADDED PROFILES / APPS
        i = 0
        for key in profiles:
            self.new_tab = qtw.QWidget()
            #self.tabWidget.addTab(self.new_tab, key)
            #self.new_tab.setObjectName(f"{key}{i}")
            self.tabWidget.addTab(self.new_tab, key)
            #self.tabWidget.addTab(self.tabWidget.findChild(f"{key}{i}"), key)

            self.newTab_listWidget = qtw.QListWidget(self.new_tab)
            self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))

            for item in profiles[key]:
                self.newTab_listWidget.addItem(item)

            self.new_tab.setObjectName(f"{key}{i}")
            self.newTab_listWidget.setObjectName(f"newTab_listWidget{i}")

            i += 1
            

            #list_name = f"{key}_list"
            #self.tab_listWidget = qtw.QListWidget(self.tabWidget)
            #QListWidget.setObjectName(self, list_name)
            #self.list_name = qtw.QListWidget(self.new_tab)
            #self.list_name.setGeometry(qtc.QRect(20, 10, 281, 441))

            for app in profiles[key]:
            #    self.list_name.addItem(app)
                apps.append(app)
            
        
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
        self.launchButton.clicked.connect(self.launch)
        
        # TEST

        #5 i = 0
#5 
        #5 self.new_tab1 = qtw.QWidget()
        #5 self.tabWidget.addTab(self.new_tab1, f"new1")
#5 
        #5 self.new_tab2 = qtw.QWidget()
        #5 self.tabWidget.addTab(self.new_tab2, "new2")
#5 
        #5 self.newTab_listWidget = qtw.QListWidget(self.new_tab1)
        #5 self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
        #5 self.newTab_listWidget.setObjectName(f"newTab_listWidget{i}")
#5 
        #5 i += 1
#5 
        #5 self.newTab_listWidget = qtw.QListWidget(self.new_tab2)
        #5 self.newTab_listWidget.setGeometry(qtc.QRect(20, 10, 281, 441))
        #5 self.newTab_listWidget.setObjectName(f"newTab_listWidget{i}")




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

            # i = tabwidget.getindexof the just created tab
            i = self.tabWidget.indexOf(self.new_tab)

            self.new_tab.setObjectName(f"{key}{i}")
            self.newTab_listWidget.setObjectName(f"newTab_listWidget{i}")

            #i = 0
            #for profile in range(len(profiles)):
            #    self.newTab_listWidget = qtw.QListWidget(self.new_tab)
            #    self.newTab_listWidget.setObjectName(f"{i}")
            #    i += 1


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
        apps.append(fileName[0])
        # DUPLICATE FILE QUALIFIER
    #if fileName[0] not in apps:
        #apps.add(fileName[0])
        current_tab_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
        current_tab_index = self.tabWidget.currentIndex()
        self.current_list = self.tabWidget.findChild(QListWidget, f"newTab_listWidget{current_tab_index}")
        self.current_list.addItem(fileName[0])
        profiles[current_tab_name].append(fileName[0])
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
        #for app in apps:
        #    os.startfile(app)
        current_tab_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
        for app in profiles[current_tab_name]:
            os.startfile(app)


    def test(self):
        #print(self.tabWidget.tabText(self.tabWidget.currentIndex()))
        print(self.tabWidget.currentIndex())
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

        #print(self.tabWidget.findChildren(self.tab, "tab"))

        # 2 i = 0
        # 2 for profile in range(len(profiles)):
        # 2     list_id = i
        # 2     if i == self.tabWidget.currentIndex():
        # 2         child = self.findChild(QListWidget, f"{i}")
        # 2         print(type(child))
        # 2     i += 1


        active_list_index = self.tabWidget.currentIndex()
        #list_list = self.findChildren(QListWidget, "newTab_listWidget")
        current_list = self.findChild(QListWidget, f"newTab_listWidget{active_list_index}")
        current_list.addItem('Hello')

        # I WAS TRYING TO FIGURE OUT HOW TO PRINT THE NAME OF THE CURRENT QLIST WIDGET. MAYBE TRY RETURNING THE CHILDREN OF THE TABWIDGET.CURRENTiNDEX???

        #list_ = self.findChild(QListWidget, "tab1_listWidget")

        #for i in range(len(apps)):
        #    child = self.findChild(QListWidget, f"tabList_{i}")
        #    counter = int(child.text())
        #    child.setText(str(counter+1))



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    win = tool_window()


    win.show()


    app.exec_()