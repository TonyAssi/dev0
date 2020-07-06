from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor

    
class HomeButtonQLabel(QtWidgets.QLabel):
    clicked=QtCore.pyqtSignal()
    def __init__(self, parent):
        QtWidgets.QLabel.__init__(self, parent)
        # When hovered over, change to pointing hand cursor
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def mousePressEvent(self, ev):
        self.clicked.emit()
        