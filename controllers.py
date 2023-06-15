from views import MainView

class MainController:
    def __init__(self):
        self.view = MainView()
        self.view.button_1a.clicked.connect(self.select_1a)
        self.view.button_1b.clicked.connect(self.select_1b)
        self.view.button_sus.clicked.connect(self.select_sus)
        self.view.button_exit.clicked.connect(self.exit_program)

    def select_1a(self):
        # Lógica para seleccionar 1A
        pass

    def select_1b(self):
        # Lógica para seleccionar 1B
        pass

    def select_sus(self):
        # Lógica para seleccionar SUS
        pass

    def exit_program(self):
        self.view.close()
