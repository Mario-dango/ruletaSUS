from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QFile, QObject
class styles():
    def __init__(self):    
        # Aplicar estilos CSS a los botones
        self.apply_styles()

    def apply_styles(self):
        style_file = QFile("styles.css")
        style_file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = style_file.readAll()
        self.setStyleSheet(str(stylesheet, encoding='utf-8'))