from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QPushButton, QVBoxLayout, QWidget, QMessageBox


class RunnerInterfaz(QMainWindow):
    def __init__(self):  # Método constructor de la clase RunnerInterfaz
        super().__init__()
        self.setWindowTitle("Sistema de Runners en el Restaurante")
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label_mesas = QLabel("Estado de las Mesas")
        self.layout.addWidget(self.label_mesas)

        self.lista_mesas = QListWidget()
        self.layout.addWidget(self.lista_mesas)

        self.boton_servir = QPushButton("Servir Mesa")
        self.boton_servir.clicked.connect(self.servir_mesa)
        self.layout.addWidget(self.boton_servir)

        self.boton_limpiar = QPushButton("Limpiar Mesa")
        self.boton_limpiar.clicked.connect(self.limpiar_mesa)
        self.layout.addWidget(self.boton_limpiar)

        self.simular_eventos()  # Simulación de eventos

    def simular_eventos(self):
        # Ejemplos de mesas que requieren servicios
        self.lista_mesas.addItem("Mesa 1")
        self.lista_mesas.addItem("Mesa 2")
        self.lista_mesas.addItem("Mesa 3")

        # Ejemplos de comandas listas para servir
        self.comandas_listas = ["Comanda 1", "Comanda 2"]

    def servir_mesa(self):  # Realizar acciones para servir la mesa según el número de mesa seleccionado
        mesa_seleccionada = self.lista_mesas.currentItem()
        if mesa_seleccionada:
            numero_mesa = mesa_seleccionada.text()
            self.mostrar_dialogo_informativo(f"Sirviendo mesa {numero_mesa}")
            
            if numero_mesa in self.comandas_listas:
                self.comandas_listas.remove(numero_mesa)
                self.mostrar_dialogo_informativo(f"Comanda {numero_mesa} entregada a los comensales")
            else:
                self.mostrar_dialogo_informativo(f"No hay comanda lista para la mesa {numero_mesa}")

    def limpiar_mesa(self):  # Realizar acciones para limpiar la mesa según el número de mesa seleccionado
        mesa_seleccionada = self.lista_mesas.currentItem()
        if mesa_seleccionada:
            numero_mesa = mesa_seleccionada.text()
            self.mostrar_dialogo_informativo(f"Limpiando mesa {numero_mesa}")
            self.lista_mesas.takeItem(self.lista_mesas.currentRow())
            self.mostrar_dialogo_informativo(f"Mesa {numero_mesa} liberada y lista para nuevos comensales")

    def mostrar_dialogo_informativo(self, mensaje):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Información")
        dialogo.setText(mensaje)
        dialogo.setIcon(QMessageBox.Icon.Information)
        dialogo.exec()


if __name__ == "__main__":
    app = QApplication([])
    ventana = RunnerInterfaz()
    ventana.show()
    app.exec()


