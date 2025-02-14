from math_recognition import gui_layout, make_expression
from PyQt5.QtCore import QObject, Qt, pyqtSignal, QPoint, QSize, QRect
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class WindowGUI(QMainWindow, gui_layout.UiMainWindow):
    def __init__(self):
        super(WindowGUI, self).__init__()
        self.init_ui(self)
        self.drawingArea = DrawingArea()
        self.drawingArea.setParent(self.widget_draw)
        self.drawingArea.resize(1250, 650)
        self.drawingArea.trigger.connect(self.imageReady)
        self.expression = ""

        # clear image on clicking button 'clear'
        self.button_clear.clicked.connect(self.drawingArea.clearImage)

        # submit image for results on clicking button 'submit'
        self.button_submit.clicked.connect(self.drawingArea.submitImage)

        # change mouse pen/eraser
        self.button_pen.clicked.connect(self.drawingArea.setPen)
        self.button_eraser.clicked.connect(self.drawingArea.setEraser)

        # make expression and display
        self.button_exp.clicked.connect(self.displayExpression)

    def imageReady(self):
        self.symbols_window.clear()
        symbols, exp = make_expression.prepare_from_path('img.png')
        self.expression = exp
        for symbol in symbols:
            self.symbols_window.insertPlainText(symbol.label[0] + ' ')

    def displayExpression(self):
        self.result_window.insertPlainText(self.expression + "\n")


# --- DrawingArea inherits QWidget and QObject for event manipulation ---
class DrawingArea(QWidget, QObject):
    trigger = pyqtSignal()

    def __init__(self, parent=None):
        super(DrawingArea, self).__init__()
        self.modified = False
        self.drawing = False
        self.myPenWidth = 1
        self.myPenColor = Qt.black
        self.image = QImage()
        self.lastPoint = QPoint()

    def saveImage(self, filename, fileformat):
        visible_image = self.image
        if visible_image.save(filename, fileformat):
            self.modified = False
            return True
        else:
            return False

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawLineTo(event.pos())
            self.drawing = False

    def resizeEvent(self, event):
        if self.width() > self.image.width() or self.height() > self.image.height():
            new_width = max(self.width() + 0, self.image.width())
            new_height = max(self.height() + 0, self.image.height())
            self.resizeImage(self.image, QSize(new_width, new_height))
            self.update()

        super(DrawingArea, self).resizeEvent(event)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        new_image = QImage(newSize, QImage.Format_RGB32)
        new_image.fill(Qt.white)
        painter = QPainter(new_image)
        painter.drawImage(QPoint(0, 0), image)
        self.image = new_image

    def submitImage(self):
        visible_image = self.image
        visible_image.save('img.png', 'PNG')
        self.trigger.emit()

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def isModified(self):
        return self.modified

    def clearImage(self):
        self.image.fill(Qt.white)
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            self.drawLineTo(event.pos())

    def paintEvent(self, event):
        painter = QPainter(self)
        dirty_rect = event.rect()
        painter.drawImage(dirty_rect, self.image, dirty_rect)

    def drawLineTo(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        rad = self.myPenWidth / 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = QPoint(endPoint)

    def setPen(self):
        self.setPenColor(Qt.black)
        self.setPenWidth(1)

    def setEraser(self):
        self.setPenColor(Qt.white)
        self.setPenWidth(30)

    def print_(self):
        printer = QPrinter(QPrinter.HighResolution)

        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth