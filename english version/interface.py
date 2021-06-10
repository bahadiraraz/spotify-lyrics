import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 800)
        MainWindow.setAnimated(True)
        MainWindow.setWindowIcon(QtGui.QIcon(rf"./son5.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lyrics = QtWidgets.QTextBrowser(self.centralwidget)
        self.lyrics.setGeometry(QtCore.QRect(10, 60, 731, 720))
        self.lyrics.setObjectName("lyrics")
        self.song_name = QtWidgets.QLabel(self.centralwidget)
        self.song_name.setGeometry(QtCore.QRect(11, 20, 400, 31))
        self.song_name.setText("")
        self.song_name.setObjectName("song_name")
        self.bahadir = QtWidgets.QLabel(self.centralwidget)
        self.bahadir.setGeometry(QtCore.QRect(685, 30, 60, 16))
        self.bahadir.setObjectName("bahadir")
        self.bahadir2 = QtWidgets.QLabel(self.centralwidget)
        self.bahadir2.setGeometry(QtCore.QRect(614, 30, 70, 16))
        self.bahadir2.setObjectName("bahadir2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "soptify lyrics-ENG"))
        self.song_name.setText(_translate("MainWindow", "waiting for song..."))

        self.bahadir2.setText("Developed by ")
        self.bahadir.setText('<a href="https://github.com/BAHADIR54"> BAHADIR54</a>')
        self.bahadir.setOpenExternalLinks(True)

