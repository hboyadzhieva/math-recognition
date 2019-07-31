from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QPushButton, QPlainTextEdit


class UiMainWindow(object):
    def init_ui(self, MainWindow):
        # main GUI window ------------------------------------------------
        MainWindow.setGeometry(220, 80, 1300, 900)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumHeight(900)
        MainWindow.setMaximumHeight(900)
        MainWindow.setMinimumWidth(1300)
        MainWindow.setMaximumWidth(1300)
        MainWindow.setStyleSheet("QWidget {background-color:rgb(180,180,180)}")

        # drawing area------------------------------------
        self.widget_draw = QWidget(MainWindow)
        self.widget_draw.setObjectName("widget_draw")
        self.widget_draw.setGeometry(25, 25, 1250, 650)
        self.widget_draw.setStyleSheet("QWidget {background-color: rgb(255,255,255)}")
        self.widget_draw.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

        # button submit -----------------------------
        self.button_submit = QPushButton('Submit', MainWindow)
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

        # button clear -----------------------------
        self.button_clear = QPushButton('Clear', MainWindow)
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

        # button make expression -----------------------------
        self.button_exp = QPushButton('Make Expression', MainWindow)
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

        # icons for buttons -----------------------------
        penIcon = QtGui.QIcon()
        penIcon.addPixmap(QtGui.QPixmap('../data/pen.png'))
        eraseIcon = QtGui.QIcon()
        eraseIcon.addPixmap(QtGui.QPixmap('../data/eraser.png'))

        # button pen -----------------------------
        self.button_pen = QPushButton('', MainWindow)
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
        self.button_pen.setIcon(penIcon)

        # button eraser -----------------------------
        self.button_eraser = QPushButton('', MainWindow)
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
        self.button_eraser.setIcon(eraseIcon)

        # result window
        self.result_window = QPlainTextEdit(MainWindow)
        self.result_window.setObjectName("result_window")
        self.result_window.setGeometry(25, 750, 950, 100)
        self.result_window.setStyleSheet("QWidget {background-color:white; font-size:15pt}")

        # single symbols window
        self.symbols_window = QPlainTextEdit(MainWindow)
        self.symbols_window.setObjectName("symbols_window")
        self.symbols_window.setGeometry(1075, 750, 200, 100)
        self.symbols_window.setStyleSheet("QWidget {background-color:white; font-size:12pt}")

