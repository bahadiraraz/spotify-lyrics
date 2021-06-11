import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 800)
        MainWindow.setAnimated(True)
        MainWindow.setWindowIcon(QtGui.QIcon(rf"{os.getcwd()}\son5.ico"))
        MainWindow.setStyleSheet(";\n"
                                 "background-color: rgb(54,54,54);"
                                 "border: 1px solid rgb(54,54,54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lyrics = QtWidgets.QTextBrowser(self.centralwidget)
        self.lyrics.setObjectName("lyrics")
        self.scrrolll = QtWidgets.QScrollBar(self.centralwidget)
        self.scrrolll.setStyleSheet("QScrollBar:vertical" "{"
                                    "border: 1px solid rgb(54,54,54);"
                                    "background:rgb(54,54,54);"
                                    "width:14px;"

                                    "margin: 0px 0px 0px 0px;"
                                    "}"
                                    "QScrollBar::handle:vertical {"
                                    "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
                                    "stop: 0 #202225, stop: 0.5 #202225, stop:1 #202225);"
                                    "min-height: 0px;"
                                    "margin: 0px 1px 0px 1px;"
                                    "width: 10px;"
                                    "border-width: 2px;"
                                    "border-radius: 5px;"

                                    "}"
                                    "QScrollBar::add-line:vertical {"
                                    "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
                                    "stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
                                    "height: 0px;"
                                    "subcontrol-position: bottom;"
                                    "subcontrol-origin: margin;"
                                    "}"
                                    "QScrollBar::sub-line:vertical {"
                                    "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
                                    "stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
                                    "height: 0 px;"
                                    "subcontrol-position: top;"
                                    "subcontrol-origin: margin;"
                                    "}"
                                    "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical" "{"
                                    "background: #2e3338;"
                                    "border-width: 2px;"
                                    "border-radius: 5px;"

                                    "}"
                                    )
        self.lyrics.setVerticalScrollBar(self.scrrolll)
        self.lyrics.setStyleSheet("color: rgb(255,255,255)")
        self.lyrics.setFont(QFont('Times', 10))

        self.song_name = QtWidgets.QLabel(self.centralwidget)
        self.song_name.setText("")
        self.song_name.setObjectName("song_name")
        self.song_name.setStyleSheet("color: rgb(255,255,255);")
        self.song_name.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.bahadir = QtWidgets.QLabel(self.centralwidget)
        self.bahadir.setObjectName("bahadir")

        self.bahadir2 = QtWidgets.QLabel(self.centralwidget)
        self.bahadir2.setObjectName("bahadir2")
        self.bahadir2.setStyleSheet("color: rgb(255,255,255);")

        self.bahadir3 = QtWidgets.QLabel(self.centralwidget)
        self.bahadir3.setObjectName("bahadir3")
        self.bahadir3.setStyleSheet("color: rgb(255,255,255);")

        MainWindow.setCentralWidget(self.centralwidget)
        self.v_box=QtWidgets.QVBoxLayout()
        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.song_name, alignment=Qt.AlignBottom,stretch=0)
        self.h_box.setContentsMargins(1,10,1,1)
        self.h_box.addWidget(self.bahadir2, alignment=Qt.AlignRight,stretch=1)
        self.h_box.addWidget(self.bahadir, alignment=Qt.AlignRight,stretch=0)

        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.bahadir3, alignment=Qt.AlignBottom, stretch=0)
        self.v_box.addWidget(self.lyrics)
        self.centralwidget.setLayout(self.v_box)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "soptify lyrics-ENG"))
        self.song_name.setText(_translate("MainWindow", "waiting for song..."))
        self.song_name.setFont(QFont('Times', 12,weight=QtGui.QFont.Bold))
        self.bahadir3.setText(_translate("MainWindow", "_" * (len("waiting for song...") - 2)))
        self.bahadir3.setFont(QFont('Times', 12, weight=QtGui.QFont.Bold))
        self.bahadir2.setText("Developed by")
        self.bahadir2.setFont(QFont('Times', 10))
        self.bahadir.setText("<a href='https://github.com/BAHADIR54' style='color:{}'> BAHADIR54</a>".format("#FFFFFF"))
        self.bahadir.setFont(QFont('Times', 10))
        self.bahadir.setOpenExternalLinks(True)



