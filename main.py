from PyQt5.QtWidgets import QApplication
from controllers import MainController
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec())
