from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de Curso")
        self.setGeometry(100, 100, 800, 600)

        # Cargar la imagen de fondo
        pixmap = QPixmap("img/fondo1.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 800, 600)

        # Etiqueta "En qué curso estamos profe"
        self.label = QLabel("En qué curso estamos profe", self)
        self.label.setGeometry(100, 100, 600, 50)
        self.label.setStyleSheet("font-size: 20px;")

        # Botones
        self.button_1a = QPushButton("1A", self)
        self.button_1a.setGeometry(100, 200, 200, 50)
        self.button_1b = QPushButton("1B", self)
        self.button_1b.setGeometry(100, 300, 200, 50)
        self.button_sus = QPushButton("Seleccionar SUS", self)
        self.button_sus.setGeometry(100, 400, 200, 50)

        self.button_exit = QPushButton("Salir", self)
        self.button_exit.setGeometry(600, 500, 100, 50)
