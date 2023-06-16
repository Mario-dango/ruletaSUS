from PyQt5.QtCore import QObject
from views import MainView, DifficultyView

class MainController(QObject):
    def __init__(self):
        super().__init__()

        self.main_view = MainView()
        self.difficulty_view = DifficultyView()

        self.main_view.button_1A.clicked.connect(self.show_difficulty_window)
        self.difficulty_view.button_exit.clicked.connect(self.show_main_window)
        self.main_view.button_exit.clicked.connect(self.close_main_window)

    def close_main_window(self):
        self.difficulty_view.close()
        self.main_view.close()

    def show_main_window(self):
        self.difficulty_view.close()
        self.main_view.show()

    def show_difficulty_window(self):
        self.main_view.close()
        self.difficulty_view.show()
