import functions
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication,QMainWindow, QMenu, QAction, QSystemTrayIcon,qApp
from interface import Ui_MainWindow
from PyQt5.QtGui import QIcon
import time

class SongSelection(QThread):
    song_name = pyqtSignal(str)
    lyrics = pyqtSignal(str)
    error = pyqtSignal(str)
    le = pyqtSignal(int)
    def __init__(self):
        super().__init__()
    def run(self):
        flag = None
        flag2 = None
        while True:
            try:
                song_info = functions.song_find()

                if song_info[0] != flag and song_info[1] != '' and song_info != "spotify kapalı":
                    data = f"{song_info[0]} {song_info[1]}"
                    le = len(data)
                    lyrics = functions.get_lyrics(song=song_info[0], artist=song_info[1].split(",")[0])
                    self.song_name.emit(data)
                    self.lyrics.emit(lyrics)
                    self.le.emit(le)
                    flag = song_info[0]
                    flag2 = song_info[1]

                elif song_info == ['Spotify',""] and flag2 == None:
                    self.error.emit("şarkı bekleniyor...")
                elif song_info == "spotify kapalı":
                    flag = None
                    flag2 = None
                    self.lyrics.emit("")
                    self.error.emit("spotify kapalı")
            except Exception:
                pass
            time.sleep(0.3)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.song = SongSelection()
        self.song.song_name.connect(lambda data: self.ui.song_name.setText(str(data)))
        self.song.lyrics.connect(lambda lyrics: self.ui.lyrics.setText(str(lyrics)))
        self.song.error.connect(lambda error: self.ui.song_name.setText(str(error)))
        self.song.le.connect(lambda le: self.ui.bahadir3.setText(str(("_"*le))))
        self.song.start()
        self.tray_icon = QSystemTrayIcon(self)
        self.icon5 = QIcon("son5.ico")
        self.tray_icon.setIcon(self.icon5)
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
