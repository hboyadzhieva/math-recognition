from math_recognition import gui_layout
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel
from PyQt5 import QtGui, QtCore

class WindowGUI(QMainWindow, gui_layout.UiMainWindow):
    def __init__(self):
        super(WindowGUI, self).__init__()
        self.init_ui(self)
        self.drawing_area = DrawingArea()
        self.drawing_area.setParent(self.widget_draw)
        self.drawing_area.resize(1250, 650)



# --- DrawingArea inherits QWidget and QObject for event manipulation ---
class DrawingArea(QWidget, QObject):
    def __init__(self):
        super(DrawingArea, self).__init__()
        self.mouse_pressed = False
        # --- Because QImage is a QPaintDevice subclass, QPainter can be used to draw directly onto images ---
        self.my_image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.my_image.fill(Qt.white)
        self.pen_color = Qt.black
        self.pen_size = 1
        self.last_point = QtCore.QPoint()



    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.last_point = QWidget.mapFromGlobal(self, QtGui.QCursor.pos())
            self.mouse_pressed = True

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() & Qt.LeftButton & self.mouse_pressed:
            painter = QtGui.QPainter(self.my_image)
            painter.setPen(QtGui.QPen(self.pen_color, self.pen_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            # --- QCursor.pos() returns the position of the cursor of the primary screen in global screen coordinates ---
            # --- use mapFromGlopbal to Map to QWidget coordinates ---
            new_point = QWidget.mapFromGlobal(self, QtGui.QCursor.pos())
            painter.drawLine(self.last_point, new_point)
            self.last_point = new_point
            self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.mouse_pressed = False

    def paintEvent(self, QPaintEvent):
        canvasPainter = QtGui.QPainter(self)
        canvasPainter.drawImage(self.rect(), self.my_image, self.my_image.rect())





