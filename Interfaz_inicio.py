import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QDialog, QMessageBox
from Interfaz_anfitrion import AnfitrionInterfaz
from Interfaz_garzon import GarzonInterfaz
from Interfaz_bartender import VentanaBartender

class RegistroVentana(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.contrasena_label = QLabel("Contraseña:")
        self.contrasena_input = QLineEdit()
        self.contrasena_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.contrasena_label2 = QLabel("Confirmar contraseña:")
        self.contrasena_input2 = QLineEdit()
        self.contrasena_input2.setEchoMode(QLineEdit.EchoMode.Password)
        self.opcion_label = QLabel("Opción:")
        self.opcion_combo = QComboBox()
        self.opcion_combo.addItems(["Anfitrión", "Garzón", "Chef", "Bartender", "Runner"])
        self.registrar_button = QPushButton("Registrar")
        self.registrar_button.clicked.connect(self.registrar_usuario)

        main_layout.addWidget(self.nombre_label)
        main_layout.addWidget(self.nombre_input)
        main_layout.addWidget(self.contrasena_label)
        main_layout.addWidget(self.contrasena_input)
        main_layout.addWidget(self.contrasena_label2)
        main_layout.addWidget(self.contrasena_input2)
        main_layout.addWidget(self.opcion_label)
        main_layout.addWidget(self.opcion_combo)
        main_layout.addWidget(self.registrar_button)

    def registrar_usuario(self):
        nombre = self.nombre_input.text()
        contrasena = self.contrasena_input.text()
        cargo = self.opcion_combo.currentText()
        if contrasena == self.contrasena_input2.text():
            #registrar
            #trabajar string cargo
            cargo = cargo.replace("ó","o")
            registro = f"{nombre},{contrasena},{cargo.lower()}\n"
            archivo = open(f"{os.path.dirname(__file__)}/data/registros.csv","a+")
            archivo.write(registro)
            archivo.close()
            QMessageBox.information(self, "Exito", "El usuario ha sido registrado", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            self.accept()
        else:
            QMessageBox.warning(self,"Error", "Las contraseñas deben ser identicas", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

class LoginVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.contrasena_label = QLabel("Contraseña:")
        self.contrasena_input = QLineEdit()
        self.contrasena_input.setEchoMode(QLineEdit.EchoMode.Password)
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
        ventana_registro = RegistroVentana()
        if ventana_registro.exec() == QDialog.accepted:
            self.nombre_input.clear()
            self.contrasena_input.clear()

    def iniciar_sesion(self):
        nombre = self.nombre_input.text()
        contrasena = self.contrasena_input.text()
        archivo = open(f"{os.path.dirname(__file__)}/data/registros.csv", "r")
        existe = False
        for linea in archivo:
            #verificar si el usuario existe
            aux = linea.split(",")
            if nombre == aux[0]:
                existe = True
                break
            else:
                continue
        if existe == True:
            #buscar la contraseña y autorizar
            if contrasena == aux[1]:
                #Loguear
                self.llamar_ventana(aux[2][:-1],aux[0])
            else:
                QMessageBox.warning(self,"Error", "La contraseña es incorrecta", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else:
            QMessageBox.warning(self,"Error", "Usuario no registrado", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                
    
    def llamar_ventana(self,modo, usuario=None):
        if modo == "anfitrion":
            print(modo)
            self.interfaz_anfitrion = AnfitrionInterfaz()
            self.interfaz_anfitrion.show()
            self.hide()
        elif modo == "garzon":
            print(modo)
            self.interfaz_garzon = GarzonInterfaz()
            self.interfaz_garzon.show()
            self.hide()
        elif modo == "bartender":
            print(modo)
            self.interfaz_bartender = VentanaBartender(usuario)
            self.interfaz_bartender.show()


if __name__ == "__main__":
    ruta = os.path.dirname(__file__)
    try:
        os.mkdir(f"{ruta}/data")
    except FileExistsError:
        pass

    archivos = ["registros.csv","comandas.csv"]
    for archivo in archivos:
        try:
            temp = open(f"{ruta}/data/{archivo}","x")
            temp.close()
        except FileExistsError:
            pass

    app = QApplication(sys.argv)
    ventana = LoginVentana()
    ventana.show()
    sys.exit(app.exec())