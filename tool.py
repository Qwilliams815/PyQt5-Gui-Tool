# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.proButton = QtWidgets.QPushButton(self.centralwidget)
        self.proButton.setGeometry(QtCore.QRect(70, 70, 75, 23))
        self.proButton.setObjectName("proButton")
        self.appButton = QtWidgets.QPushButton(self.centralwidget)
        self.appButton.setGeometry(QtCore.QRect(70, 170, 75, 23))
        self.appButton.setObjectName("appButton")
        self.launchButton = QtWidgets.QPushButton(self.centralwidget)
        self.launchButton.setGeometry(QtCore.QRect(70, 280, 75, 23))
        self.launchButton.setObjectName("launchButton")
        self.proNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.proNameEdit.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.proNameEdit.setObjectName("proNameEdit")
        self.seperate_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.seperate_listWidget.setGeometry(QtCore.QRect(210, 40, 201, 481))
        self.seperate_listWidget.setObjectName("seperate_listWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(440, 40, 321, 491))
        self.tabWidget.setObjectName("tabWidget")
        #self.tab = QtWidgets.QWidget()
        #self.tab.setObjectName("tab")
        #self.tab1_listWidget = QtWidgets.QListWidget(self.tab)
        #self.tab1_listWidget.setGeometry(QtCore.QRect(20, 10, 281, 441))
        #self.tab1_listWidget.setObjectName("tab1_listWidget")
        #self.tabWidget.addTab(self.tab, "")
        #self.tab_2 = QtWidgets.QWidget()
        #self.tab_2.setObjectName("tab_2")
        #self.tab2_listWidget = QtWidgets.QListWidget(self.tab_2)
        #self.tab2_listWidget.setGeometry(QtCore.QRect(20, 10, 281, 441))
        #self.tab2_listWidget.setObjectName("tab2_listWidget")
        #self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.proButton.setText(_translate("MainWindow", "Add Profile"))
        self.appButton.setText(_translate("MainWindow", "Add App"))
        self.launchButton.setText(_translate("MainWindow", "Launch"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
