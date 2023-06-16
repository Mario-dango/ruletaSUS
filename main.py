from PyQt5.QtWidgets import QApplication
from controllers import MainController

if __name__ == "__main__":
    app = QApplication([])
    controller = MainController()
    controller.show_main_window()
    app.exec_()
