import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QDialog

class RegistroVentana(QDialog):
    def __init__(self, registro):
        super().__init__()
        self.registro = registro
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.contrasena_label = QLabel("Contraseña:")
        self.contrasena_input = QLineEdit()
        self.opcion_label = QLabel("Opción:")
        self.opcion_combo = QComboBox()
        self.opcion_combo.addItems(["Opción 1", "Opción 2", "Opción 3"])
        self.registrar_button = QPushButton("Registrar")
        self.registrar_button.clicked.connect(self.registrar_usuario)

        main_layout.addWidget(self.nombre_label)
        main_layout.addWidget(self.nombre_input)
        main_layout.addWidget(self.contrasena_label)
        main_layout.addWidget(self.contrasena_input)
        main_layout.addWidget(self.opcion_label)
        main_layout.addWidget(self.opcion_combo)
        main_layout.addWidget(self.registrar_button)

    def registrar_usuario(self):
        nombre = self.nombre_input.text()
        contrasena = self.contrasena_input.text()
        opcion = self.opcion_combo.currentText()

        self.registro[nombre] = {"contrasena": contrasena, "opcion": opcion}
        print("Usuario registrado:", nombre)
        self.accept()


class LoginVentana(QWidget):
    def __init__(self, registro):
        super().__init__()
        self.registro = registro
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.contrasena_label = QLabel("Contraseña:")
        self.contrasena_input = QLineEdit()
        self.iniciar_button = QPushButton("Iniciar Sesión")
        self.iniciar_button.clicked.connect(self.iniciar_sesion)
        self.registrar_button = QPushButton("Registrar Usuario")
        self.registrar_button.clicked.connect(self.mostrar_ventana_registro)

        main_layout.addWidget(self.nombre_label)
        main_layout.addWidget(self.nombre_input)
        main_layout.addWidget(self.contrasena_label)
        main_layout.addWidget(self.contrasena_input)
        main_layout.addWidget(self.iniciar_button)
        main_layout.addWidget(self.registrar_button)

    def mostrar_ventana_registro(self):
        ventana_registro = RegistroVentana(self.registro)
        if ventana_registro.exec() == QDialog.accepted:
            self.nombre_input.clear()
            self.contrasena_input.clear()

    def iniciar_sesion(self):
        nombre = self.nombre_input.text()
        contrasena = self.contrasena_input.text()

        if nombre in self.registro and self.registro[nombre]["contrasena"] == contrasena:
            opcion = self.registro[nombre]["opcion"]
            print("Inicio de sesión exitoso.")
            print("Nombre:", nombre)
            print("Opción seleccionada:", opcion)
        else:
            print("Error en el inicio de sesión.")

        self.nombre_input.clear()
        self.contrasena_input.clear()


class InterfazPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz Principal")
        self.setGeometry(100, 100, 400, 200)

        self.MainWindow = None

        self.main_layout = QVBoxLayout()
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

        registro = {}
        login_widget = LoginVentana(registro)
        self.main_layout.addWidget(login_widget)

