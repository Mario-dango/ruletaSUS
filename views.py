from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QFile

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ruleta SUS")
        self.setFixedSize(800, 600)

        # Fondo
        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 800, 600)
        background_image = QPixmap("img/sus_mamadisimo.jpg")
        background_label.setPixmap(background_image)
        background_label.setScaledContents(True)

        # Etiqueta "En que curso estamos profe"
        label = QLabel(self)
        label.setText("En qué curso estamos profe")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(200, 100, 400, 30)

        # Botones
        self.button_1A = QPushButton(self)
        self.button_1A.setText("1A")
        self.button_1A.setGeometry(300, 200, 200, 50)

        self.button_1B = QPushButton(self)
        self.button_1B.setText("1B")
        self.button_1B.setGeometry(300, 300, 200, 50)

        self.button_select = QPushButton(self)
        self.button_select.setText("Seleccionar SUS")
        self.button_select.setGeometry(250, 400, 300, 50)

        self.button_exit = QPushButton(self)
        self.button_exit.setText("Salir")
        self.button_exit.setGeometry(700, 550, 80, 30)
        
        # Aplicar estilos CSS a los botones
        self.apply_styles()

    def apply_styles(self):
        style_file = QFile("styles.css")
        style_file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = style_file.readAll()
        self.setStyleSheet(str(stylesheet, encoding='utf-8'))

class DifficultyView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ruleta SUS")
        self.setFixedSize(800, 600)

        # Fondo
        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 800, 600)
        background_image = QPixmap("img/kinda_sus.jpg")
        background_label.setPixmap(background_image)
        background_label.setScaledContents(True)

        # Etiqueta "Qué dificultad desea elegir"
        label = QLabel(self)
        label.setText("Qué dificultad desea elegir")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(200, 100, 400, 30)

        # Botones de dificultad
        self.button_easy = QPushButton(self)
        self.button_easy.setText("Fácil")
        self.button_easy.setGeometry(300, 200, 200, 50)

        self.button_medium = QPushButton(self)
        self.button_medium.setText("Medio")
        self.button_medium.setGeometry(300, 300, 200, 50)

        self.button_hard = QPushButton(self)
        self.button_hard.setText("Difícil")
        self.button_hard.setGeometry(300, 400, 200, 50)

        # Botón de salida
        self.button_exit = QPushButton(self)
        self.button_exit.setText("Salir")
        self.button_exit.setGeometry(700, 550, 80, 30)

        # Aplicar estilos CSS a los botones
        self.apply_styles()

    def apply_styles(self):
        style_file = QFile("styles.css")
        style_file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = style_file.readAll()
        self.setStyleSheet(str(stylesheet, encoding='utf-8'))