
from PyQt5 import QtGui, QtWidgets
from gui import MainWindow
import constants
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(constants.ICON))
    MainWindow().show()
    sys.exit(app.exec_())
    