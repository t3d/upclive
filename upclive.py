#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt4 import QtGui, QtCore

__license__ = 'GPL 3'
__copyright__ = '2011, Tomasz Długosz <tomek3d@gmail.com>'

vlc_opts = '--rtsp-tcp --rtsp-wmserver --rtsp-caching=5000 --clock-synchro=0  --aspect-ratio=16:9'

vlc_bin = 'vlc'

channels = {
  'Animal Planet':'rtsp://stream.livetv.chello.pl/Animal',
  'Discovery':'rtsp://stream.livetv.chello.pl/Discovery',
  'CNN':'rtsp://stream.livetv.chello.pl/CNN',
  'TVN 24':'rtsp://stream.livetv.chello.pl/TVN24',
  'MiniMini+':'rtsp://stream.livetv.chello.pl/MiniMini',
  'teleTOON+':'rtsp://stream.livetv.chello.pl/ZigZap',
  'National Geographic':'rtsp://stream.livetv.chello.pl/NATGEO'
  }

class Interface(QtGui.QWidget):
    
    def __init__(self):
        super(Interface, self).__init__()
        
        self.initUI()
        
    def play(self):
        sender = self.sender()
        channel_name = sender.text()
        print channel_name
        url = channels[str(channel_name)]
        print url

        os.system(vlc_bin + ' ' + vlc_opts + ' ' + url)

    def initUI(self):
        
        #settingsButton = QtGui.QPushButton("Ustawienia")
        quitButton = QtGui.QPushButton(u'Wyjście')

        hbox = QtGui.QHBoxLayout()
        #hbox.addWidget(settingsButton)
        hbox.addStretch(1)
        hbox.addWidget(quitButton)

        vbox = QtGui.QVBoxLayout()
        for channel_name in channels.keys():
            btn = QtGui.QPushButton(channel_name)
            btn.clicked.connect(self.play)
            vbox.addWidget(btn)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    

        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
        self.setGeometry(100, 300, 100, 150)
        self.setWindowTitle('upclive')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

