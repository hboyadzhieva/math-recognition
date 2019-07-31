from math_recognition import gui_functionality, gui_layout
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui_functionality.WindowGUI()
    window.show()
    print(window.__dict__)
    print("asha")
    sys.exit(app.exec_())
