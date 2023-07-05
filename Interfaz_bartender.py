import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTableView, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtCore import QTimer
from clases import Comanda
from datetime import datetime

class VentanaBartender(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.setWindowTitle("Bartender")
        self.usuario_actual = usuario
        #Elementos
        bienvenida = QLabel(f"Bienvenido {self.usuario_actual}")
        titulo = QLabel("Comandas actuales")
        self.tabla = QTableView()
        self.hora_actual = QLabel(f"Hora actual: {datetime.now().strftime('%H:%M:%S')}")

        #Layouts
        #Hora y titulo
        hora_titulo = QHBoxLayout()
        hora_titulo.addWidget(titulo)
        hora_titulo.addWidget(self.hora_actual)

        hora_titulo_widget = QWidget()
        hora_titulo_widget.setLayout(hora_titulo)

        layout = QVBoxLayout()
        layout.addWidget(bienvenida)
        layout.addWidget(hora_titulo_widget)
        layout.addWidget(self.tabla)
        
        layout_widget = QWidget()
        
        layout_widget.setLayout(layout)

        self.setCentralWidget(layout_widget)

        #Pieza de codigo que hace funcionar el reloj de hora actual
        self.update = QTimer()
        self.update.timeout.connect(self.actualizar_hora)
        self.update.start(1000)
    
    def actualizar_hora(self):
        self.hora_actual.setText(f"Hora actual: {datetime.now().strftime('%H:%M:%S')}")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaBartender("Vicente")
    window.show()
    app.exec()
