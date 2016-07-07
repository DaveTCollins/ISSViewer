import requests
import sys
import thread
import time

from PySide import QtGui, QtCore

data = {}

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
        timer.setInterval(1000)
        timer.timeout.connect(self.myupdate)
        timer.start()

    def myupdate(self):
        val = self.function()
        self.setText(str(val))

def get_latitude():
    return data['iss_position']['latitude']

def get_longitude():
    return data['iss_position']['longitude']

def fetch_data():
    while True:
        get_data()
        time.sleep(1)

def get_data():
    global data
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = r.json()


app = QtGui.QApplication([])
win = Window()

main_frame = QtGui.QFrame(win)
win.setCentralWidget(main_frame)
main_frame_layout = QtGui.QVBoxLayout(main_frame)

lat_label = RequestLabel(get_latitude)
lon_label = RequestLabel(get_longitude)
main_frame_layout.addWidget(lat_label)
main_frame_layout.addWidget(lon_label)


thread.start_new_thread(fetch_data, ())
win.show()
sys.exit(app.exec_())

