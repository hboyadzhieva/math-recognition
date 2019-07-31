from math_recognition import gui_layout,make_expression
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QMainWindow


class WindowGUI(QMainWindow, gui_layout.UiMainWindow):
    def __init__(self):
        super(WindowGUI, self).__init__()
        self.init_ui(self)
        self.drawing_area_instance = DrawingArea()
        self.drawing_area_instance.setParent(self.widget_draw)
        self.drawing_area_instance.resize(1250, 650)


# --- DrawingArea inherits QWidget and QObject for event manipulation ---
class DrawingArea(QWidget, QObject):
    trigger = pyqtSignal()
    def __init__(self):
        super(DrawingArea, self).__init__()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print(QMouseEvent.button())