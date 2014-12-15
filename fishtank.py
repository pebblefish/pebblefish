# Main application panel

from PyQt5 import QtGui

class FishTank(QtGui.QWidget):
    def __init__(self):
        super(FishTank, self).__init__()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Pebblefish')
        self.setWindowIcon('images/icon.png')

        self.show()
