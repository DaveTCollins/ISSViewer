import requests
import sys

from PySide import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self, parent=None, flags=QtCore.Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 1920, 360)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

class RequestLabel(QtGui.QLabel):

    def __init__(self, function):
        self.function = function
        QtGui.QLabel.__init__(self, '0')
        timer = QtCore.QTimer(self)
        timer.setInterval(5000)
        timer.timeout.connect(self.myupdate)
        timer.start()

    def myupdate(self):
        val = self.function()
        #val = int(self.text()) + 1
        self.setText(str(val))

def get_latitude():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = r.json()
    return data['iss_position']['latitude']



app = QtGui.QApplication([])
win = Window()

main_frame = QtGui.QFrame(win)
win.setCentralWidget(main_frame)
main_frame_layout = QtGui.QVBoxLayout(main_frame)

label = RequestLabel(get_latitude)
label2 = QtGui.QLabel('val2')
main_frame_layout.addWidget(label)
main_frame_layout.addWidget(label2)


win.show()
sys.exit(app.exec_())

