import sys

from PySide import QtGui, QtCore, QtWebKit

class Window(QtWebKit.QWebView):
    def __init__(self):
        QtWebKit.QWebView.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(0, 360, 640, 720)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


app = QtGui.QApplication([])
win = Window()

win.load(QtCore.QUrl('http://www.lizard-tail.com/isana/tracking/?catalog_number=25544,41639&target=iss,soyuz_m01'))

win.show()
sys.exit(app.exec_())

