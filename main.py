# always seem to need this
import sys, os, glob, subprocess, time
from pathlib import Path
# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
# This is our window from QtCreator
import mainwindow_auto

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):

        lcd = ""
        codec = ["flac", "mp3", "wav", "ogg"]
        proc = ""
        pid = ""
        my_file = ""
        pi_music = "/media/JukeBox/Music/"
        playList = pi_music+"playlist"
        playListAlbum = pi_music+"playlistAlbum"
        #pi_music = "/Users/Harbardr/Documents/DIVERS/python/JukeBox/"

        ### functions for the buttons to call
        def initText(self):
                self.playButton.setText("Play")
                self.albumButton.setText("Album")
                self.loopButton.setText("Shuffle")

        def pressedButton(self, number):
                print ("Pressed "+number)
                self.lcd = self.lcd+number
                print (self.lcd)
                self.lcdNumber.display(self.lcd)

        def pressedActionButton(self, action):
                print ("Pressed "+action)
                if action == "Del":
                        self.lcd = ""
                        self.lcdNumber.display("")
                if action == "Left":
                        self.lcd = ""
                        self.lcdNumber.display("")
                        #self.proc.communicate(input=b'<')
                if action == "Right":
                        self.lcd = ""
                        self.lcdNumber.display("")
                        #self.proc.communicate(input=b'>')
                if action == "Play":
                        if self.proc != "":
                                print (self.proc)
                                self.proc.terminate()
                                self.proc = ""
                                self.initText()
                                self.songLabel.setText("Entrez un numéro de piste")
                                print ("Pressed Stop")
                        else:
                                for iCodec in self.codec:
                                        if glob.glob(self.pi_music+self.lcd+"_*."+iCodec):
                                                print( glob.glob(self.pi_music+self.lcd+"*."+iCodec) )
                                                self.my_file = glob.glob(self.pi_music+self.lcd+"*."+iCodec)[0]
                                                self.songLabel.setText(self.my_file.rsplit("/")[-1])
                                                self.proc = subprocess.Popen(['mplayer', self.my_file])
                                                self.playButton.setText("Stop")
                                                break
                                        #else:
                                if self.my_file:
                                        self.my_file = "" 
                                else:
                                        self.songLabel.setText("Entrez un numéro de piste valide")
                                        self.my_file = ""

                        #print ("No song!")
                        self.lcd = ""
                        self.lcdNumber.display("")
                if action == "Quit":
                        if self.proc != "":
                                self.proc.terminate()
                        self.halt()
                        QtCore.QCoreApplication.instance().quit()

        def pressedLoop(self, action, album=""):
                if self.proc != "":
                        print (self.proc)
                        self.proc.terminate()
                        self.proc = ""
                        self.initText()
                        self.songLabel.setText("Entrez un numéro de piste")
                        print ("Pressed Stop")
                else:
                        if action == "Album":
                                if album:
                                        print("Pressed album")
                                        listAlbum = []
                                        for iCodec in self.codec:
                                                listAlbum.extend(glob.glob(self.pi_music+album+"*_*."+iCodec))
                                                listAlbum.sort()
                                        if listAlbum:
                                                albumTmpList = open(self.playListAlbum, "w")
                                                for song in listAlbum:
                                                        albumTmpList.write(song+"\n")
                                                albumTmpList.close()
                                                #pipes = dict(stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                                #self.proc = subprocess.Popen(['mplayer', '-playlist', self.playListAlbum], **pipes)
                                                self.proc = subprocess.Popen(['mplayer', '-playlist', self.playListAlbum])
                                                self.songLabel.setText("Lecture album "+album)
                                                self.lcdNumber.display("")
                                                self.albumButton.setText("Stop")
                                        else:
                                                self.songLabel.setText("Entrez un numéro d'album valide")
                                                self.lcd = ""
                                                self.lcdNumber.display("")

                                else:
                                        self.songLabel.setText("Entrez un numéro d'album")

                        if action == "Shuffle":
                                print("Pressed shuffle")
                                self.lcd = ""
                                self.lcdNumber.display("")
                                self.loopButton.setText("Stop")
                                self.proc = subprocess.Popen(['mplayer', '-shuffle', '-playlist', self.playList])
                                self.songLabel.setText("Mode shuffle de la musique")

        def halt(self):
                if self.proc != "":
                        self.proc.terminate()
                        self.proc = ""
                command = "/usr/bin/sudo /sbin/shutdown -h now"
                process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
                output = process.communicate()[0]
                print(output)

        def listSongs(self):
                listSongs = []
                for iCodec in self.codec:
                        listTmp = glob.glob(self.pi_music+"*."+iCodec)
                        if listTmp:
                                listSongs.extend(listTmp)
                return listSongs

        # access variables inside of the UI's file
        def __init__(self):
                super(self.__class__, self).__init__()
                self.setupUi(self) # gets defined in the UI file
                self.lcdNumber.display("")
                time.sleep(1)
                self.songLabel.setText("Entrez un numéro de piste")
                ### Hooks to for buttons
                self.push00Button.clicked.connect(lambda: self.pressedButton("0"))
                self.push01Button.clicked.connect(lambda: self.pressedButton("1"))
                self.push02Button.clicked.connect(lambda: self.pressedButton("2"))
                self.push03Button.clicked.connect(lambda: self.pressedButton("3"))
                self.push04Button.clicked.connect(lambda: self.pressedButton("4"))
                self.push05Button.clicked.connect(lambda: self.pressedButton("5"))
                self.push06Button.clicked.connect(lambda: self.pressedButton("6"))
                self.push07Button.clicked.connect(lambda: self.pressedButton("7"))
                self.push08Button.clicked.connect(lambda: self.pressedButton("8"))
                self.push09Button.clicked.connect(lambda: self.pressedButton("9"))
                self.playButton.clicked.connect(lambda: self.pressedActionButton("Play"))
                self.delButton.clicked.connect(lambda: self.pressedActionButton("Del"))
                self.loopButton.clicked.connect(lambda: self.pressedLoop("Shuffle"))
                self.albumButton.clicked.connect(lambda: self.pressedLoop("Album",self.lcd))
                self.quitButton.clicked.connect(lambda: self.pressedActionButton("Quit"))
                self.leftButton.clicked.connect(lambda: self.pressedActionButton("Left"))
                self.rightButton.clicked.connect(lambda: self.pressedActionButton("Right"))
 
# I feel better having one of these
def main():
        # a new app instance
        app = QApplication(sys.argv)

        #################
        # SLashscreen
        px = QtGui.QPixmap('/home/pi/Documents/python/JukeBox/static/jukebox.png')
        splash = QSplashScreen(px, QtCore.Qt.WindowStaysOnTopHint)
        splash.showFullScreen()
        time.sleep(3)
        app.processEvents()
        #
        ##############

        form = MainWindow()
        #form.show()
        form.showFullScreen()
        # without this, the script exits immediately.
        
        splash.finish(form)
        
        sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
        main()
