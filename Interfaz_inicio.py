import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QDialog, QMessageBox
from Interfaz_anfitrion import AnfitrionInterfaz
from Interfaz_garzon import GarzonInterfaz

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

        #Interfaces
        self.interfaz_anfitrion = AnfitrionInterfaz()
        self.interfaz_garzon = GarzonInterfaz()

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
        for linea in archivo:
            if nombre in linea:
                if contrasena in linea:
                    #iniciar sesion
                    #llevar a alguna ventana
                    linea = linea.split(",")
                    linea[2] = linea[2][:-1]
                    self.llamar_ventana(linea[2])
                    # self.hide()
                else:
                    QMessageBox.warning(self,"Error", "La contraseña es incorrecta", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                    break
            else:
                QMessageBox.warning(self,"Error", "Usuario no registrado", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                break
    
    def llamar_ventana(self,modo):
        if modo == "anfitrion":
            print(modo)
            self.interfaz_anfitrion.show()
            self.hide()
        elif modo == "garzon":
            print(modo)
            self.interfaz_garzon.show()
            self.hide()

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

        login_widget = LoginVentana()
        self.main_layout.addWidget(login_widget)


if __name__ == "__main__":
    ruta = os.path.dirname(__file__)
    try:
        os.mkdir(f"{ruta}/data")
    except FileExistsError:
        pass

    archivos = ["registros.csv"]
    for archivo in archivos:
        try:
            temp = open(f"{ruta}/data/{archivo}","x")
            temp.close()
        except FileExistsError:
            pass

    app = QApplication(sys.argv)
    ventana = InterfazPrincipal()
    ventana.show()
    sys.exit(app.exec())