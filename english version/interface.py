import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 800)
        MainWindow.setAnimated(True)
        MainWindow.setWindowIcon(QtGui.QIcon(rf"{os.getcwd()}\son5.ico"))
        MainWindow.setStyleSheet(";\n"
                                 "background-color: rgb(54,54,54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lyrics = QtWidgets.QTextBrowser(self.centralwidget)
        self.lyrics.setObjectName("lyrics")
        self.lyrics.setStyleSheet("color: rgb(255,255,255);")

        self.song_name = QtWidgets.QLabel(self.centralwidget)
        self.song_name.setText("")
        self.song_name.setObjectName("song_name")
        self.song_name.setStyleSheet("color: rgb(255,255,255);")

        self.bahadir = QtWidgets.QLabel(self.centralwidget)
        self.bahadir.setObjectName("bahadir")

        self.bahadir2 = QtWidgets.QLabel(self.centralwidget)
        self.bahadir2.setObjectName("bahadir2")
        self.bahadir2.setStyleSheet("color: rgb(255,255,255);")

        MainWindow.setCentralWidget(self.centralwidget)
        self.v_box=QtWidgets.QVBoxLayout()
        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.song_name, alignment=Qt.AlignBottom,stretch=0)
        self.h_box.setContentsMargins(1,10,1,1)
        self.h_box.addWidget(self.bahadir2, alignment=Qt.AlignRight,stretch=1)
        self.h_box.addWidget(self.bahadir, alignment=Qt.AlignRight,stretch=0)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.lyrics)
        self.centralwidget.setLayout(self.v_box)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "soptify lyrics-ENG"))
        self.song_name.setText(_translate("MainWindow", "waiting for song..."))
        self.bahadir2.setText("Developed by")
        self.bahadir.setText("<a href='https://github.com/BAHADIR54' style='color:{}'> BAHADIR54</a>".format("#FFFFFF"))
        self.bahadir.setOpenExternalLinks(True)



