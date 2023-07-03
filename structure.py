import sys
import Interfaz_inicio
import Interfaz_garzon
import Interfaz_anfitrion

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton, QStackedLayout, QLayout
from PyQt6.QtGui import QColor


class myWindow(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("☺")
        self.setMinimumSize(400, 200)

        # Constructor
        container0 = QWidget()
        container1 = QWidget()
        container2 = QWidget()
        container3 = QWidget()
        container4 = QWidget()
        login = QVBoxLayout(container0)
        mesas = QVBoxLayout(container1)
        garzon = QVBoxLayout(container2)
        pantalla_principal = QVBoxLayout(container4)

        # Layout y reacción
        self.main_box = QStackedLayout()

        pPrincipal = QVBoxLayout()
        pPrincipal_button0 = QPushButton("Ingresar")
        pPrincipal_button1 = QPushButton("Mesas")
        pPrincipal_button2 = QPushButton("garzon")

        pPrincipal.addWidget(pPrincipal_button0)
        pPrincipal.addWidget(pPrincipal_button1)
        pPrincipal.addWidget(pPrincipal_button2)

        pPrincipal_button0.clicked.connect(self.ir_a_0)
        pPrincipal_button1.clicked.connect(self.ir_a_1)
        pPrincipal_button2.clicked.connect(self.ir_a_2)

        pantalla_principal.addWidget(QLabel("Pantalla principal"))
        pantalla_principal.addLayout(pPrincipal)

        botonVolverP = []
        for i in range(3):
            botonVolverP += [QPushButton("Regresar")]
            botonVolverP[i].clicked.connect(self.ir_pPrincipal)

        self.current_window = None

        # Login
        self.login_window = Interfaz_inicio.InterfazPrincipal()
        self.login_window.main_layout.addWidget(botonVolverP[0])

        # Mesas
        self.mesas = Interfaz_anfitrion.AnfitrionInterfaz()
        botonVolverP[1].setParent(self.mesas)
        botonVolverP[1].setGeometry(880, 725, 100, 50)

        # Garzon
        self.mesero = Interfaz_garzon.GarzonInterfaz()
        new_widget = self.mesero.takeCentralWidget()
        new_widget.layout().addWidget(botonVolverP[2])
        self.mesero.setCentralWidget(new_widget)

        # Final

        self.main_box.addWidget(container4)
        self.main_box.addWidget(container0)
        self.main_box.addWidget(container1)
        self.main_box.addWidget(container2)
        self.main_box.addWidget(container3)

        my_window = QWidget()
        my_window.setLayout(self.main_box)
        self.setCentralWidget(my_window)

    def ir_pPrincipal(self):
        self.current_window.hide()
        self.show()
    def ir_a_0(self):
        self.hide()
        self.login_window.show()
        self.current_window = self.login_window
    def ir_a_1(self):
        self.hide()
        self.mesas.show()
        self.current_window = self.mesas
    def ir_a_2(self):
        self.hide()
        self.mesero.show()
        self.current_window = self.mesero


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()  # Obligatorio (dentro del init o fuera)
    app.exec()
