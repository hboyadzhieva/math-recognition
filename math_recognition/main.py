from math_recognition import gui_layout
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui_layout.UiMainWindow()
    sys.exit(app.exec_())
