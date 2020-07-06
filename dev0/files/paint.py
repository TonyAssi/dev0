from PyQt5 import QtCore, QtGui, QtWidgets

class Paint(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        
        
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class Paint(QtWidgets.QLabel):

    def __init__(self, parent):
        QtWidgets.QLabel.__init__(self, parent)
        
        self.width = 0
        self.height = 0

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#FFAAAA')
        
    def setup(self):
        # Get width and height
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        # Create pixmap
        pixmap = QtGui.QPixmap(self.width, self.height)
        # Set color
        pixmap.fill(QtGui.QColor(255, 255, 255))
        self.setPixmap(pixmap)
        
        

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        
        
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y-30, e.x(), e.y()-30)
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None