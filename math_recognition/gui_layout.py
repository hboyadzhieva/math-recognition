from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QPlainTextEdit
from math_recognition import make_expression


# Main window user interface
class UiMainWindow(object):
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        # --- add styling and positioning of the main window ---
        self.init_ui()
        # --- add all widgets, buttons and text areas to the main window ---
        self.drawing_area = QWidget(self.main_window)
        self.button_clear = QPushButton('Clear', self.main_window)
        self.button_submit = QPushButton('Submit', self.main_window)
        self.button_exp = QPushButton('Make Expression', self.main_window)
        self.button_pen = QPushButton('', self.main_window)
        self.button_eraser = QPushButton('', self.main_window)
        self.results_window = QPlainTextEdit(self.main_window)
        self.symbols_window = QPlainTextEdit(self.main_window)
        # --- set the styling and positions of all widgets, buttons and text areas within the window ---
        self.add_drawing_area(self.main_window)
        self.add_button_clear(self.main_window)
        self.add_button_submit(self.main_window)
        self.add_button_exp(self.main_window)
        self.add_button_pen(self.main_window)
        self.add_button_eraser(self.main_window)
        self.add_results_window(self.main_window)
        self.add_symbols_window(self.main_window)
        # --- show the main window with initialization of the object ---
        self.main_window.show()

    # --- set geometry and style of main window ---
    def init_ui(self):
        self.main_window.setGeometry(220, 80, 1300,900)
        self.main_window.setObjectName("main_window")
        self.main_window.setMinimumHeight(900)
        self.main_window.setMaximumHeight(900)
        self.main_window.setMinimumWidth(1300)
        self.main_window.setMaximumWidth(1300)
        self.main_window.setStyleSheet("QWidget {background-color:rgb(180,180,180)}")

    # --- set style and positioning of drawing area ---
    # --- drawing area is where the user draws the math expression ---
    def add_drawing_area(self, main_window):
        self.drawing_area.setObjectName("widget_draw")
        self.drawing_area.setGeometry(25, 25, 1250, 650)
        self.drawing_area.setStyleSheet("QWidget {background-color: rgb(255,255,255)}")
        self.drawing_area.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

    # --- set style and positioning of button submit ---
    # --- button submit sends the image to be transformed to its text expression equivalent ---
    def add_button_submit(self, main_window):
        self.button_submit.setObjectName("button_submit")
        self.button_submit.setGeometry(25, 680, 300, 50)
        self.button_submit.setStyleSheet("""
                QPushButton {
                    border: 2px solid #8f8f91;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
                    min-width: 80px;
                }

                QPushButton:pressed {
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
                }

                QPushButton:flat {
                    border: none; /* no border for a flat push button */
                }

                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }""")
        
    # --- set style and positioning of button clear ---
    # --- button clear clears the drawing area completely ---
    def add_button_clear(self, main_window):
        self.button_clear.setObjectName("button_clear")
        self.button_clear.setGeometry(350, 680, 300, 50)
        self.button_clear.setStyleSheet("""
                QPushButton {
                    border: 2px solid #8f8f91;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1                         #dadbde);
                    min-width: 80px;
                }

                QPushButton:pressed {
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1                          #f6f7fa);
                }

                QPushButton:flat {
                    border: none; /* no border for a flat push button */
                }

                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }""")

    # --- set style and positioning of button expression ---
    # --- button expression builds the text expression for the image ---
    def add_button_exp(self, main_window):
       self.button_exp.setObjectName("button_exp")
       self.button_exp.setGeometry(675, 680, 300, 50)
       self.button_exp.setStyleSheet("""
                QPushButton {
                    border: 2px solid #8f8f91;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1                         #dadbde);
                    min-width: 80px;
                }

                QPushButton:pressed {
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1                          #f6f7fa);
                }

                QPushButton:flat {
                    border: none; /* no border for a flat push button */
                }

                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }""")

    # --- set style and positioning of button pen ---
    # --- chooses the current cursor to act like a pen on the drawing area---
    def add_button_pen(self, main_window):
        pen_icon = QtGui.QIcon()
        pen_icon.addPixmap(QtGui.QPixmap('images/pen.png'))
        self.button_pen.setObjectName("button_pen")
        self.button_pen.setGeometry(1075, 680, 50, 50)
        self.button_pen.setStyleSheet("""
                QPushButton {
                    border: 2px solid #8f8f91;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1                         #dadbde);
                    min-width: 80px;
                }""")
        self.button_pen.setIcon(pen_icon)

    # --- set style and positioning of button eraser ---
    # --- chooses the current cursor to act like an eraser on the drawing area ---
    def add_button_eraser(self, main_window):
        erase_icon = QtGui.QIcon()
        erase_icon.addPixmap(QtGui.QPixmap('images/eraser.png'))
        # button eraser -----------------------------
        self.button_eraser.setObjectName("button_eraser")
        self.button_eraser.setGeometry(1175, 680, 50, 50)
        self.button_eraser.setStyleSheet("""
                        QPushButton {
                            border: 2px solid #8f8f91;
                            border-radius: 6px;
                            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                              stop: 0 #f6f7fa, stop: 1                         #dadbde);
                            min-width: 80px;
                        }""")
        self.button_eraser.setIcon(erase_icon)

    # --- set style and positioning of results window ---
    # --- shows the resulting text expression that represents the expression in the image ---
    def add_results_window(self, main_window):
        self.results_window.setObjectName("results_window")
        self.results_window.setGeometry(25, 750, 950, 100)
        self.results_window.setStyleSheet("QWidget {background-color:white; font-size:15pt}")

    # --- set style and positioning of symbols window ---
    # --- shows individual recognized symbols, starting from the top-left most, until the bottom-right most ---
    def add_symbols_window(self, main_window):
        self.symbols_window.setObjectName("symbols_window")
        self.symbols_window.setGeometry(1075, 750, 200, 100)
        self.symbols_window.setStyleSheet("QWidget {background-color:white; font-size:12pt}")


class DrawingArea(QWidget):
    trigger = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(DrawingArea, self).__init__()
        self.drawing = False

    def mouseReleaseEvent(self,event: QtGui.QMouseEvent):
        if event.button() == Qt.LeftButton:
            make_expression.some_fun()

