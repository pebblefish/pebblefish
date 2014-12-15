# Main Pebblefish application
# Created by Nicholas Dyszel
# see license and readme

import fishtank
import login
from PyQt5 import QtGui
import sys

def main():
    app = QtGui.QApplication(sys.argv)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
