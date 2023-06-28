import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QComboBox, QPushButton

class MeseroInterfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz del Mesero")
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.comida_combo = self.crear_seccion_comida(main_layout)
        self.beb_combo = self.crear_seccion_bebestible(main_layout)
        self.boton_crear_pedido(main_layout)

    def crear_seccion_comida(self, layout):
        comida_group_box = QGroupBox("Comida")
        comida_layout = QVBoxLayout()

        opciones_comida = ["Seleccione la comida", "Pasta", "Ceviche", "Estofado"]  # Ejemplo de opciones de comida

        combo_box = QComboBox()
        combo_box.addItems(opciones_comida)
        comida_layout.addWidget(combo_box)

        comida_group_box.setLayout(comida_layout)
        layout.addWidget(comida_group_box)

        return combo_box

    def crear_seccion_bebestible(self, layout):
        beb_group_box = QGroupBox("Bebestibles")
        beb_layout = QVBoxLayout()

        opciones_bebida = ["Seleccione el bebestible", "Agua", "Jugo", "Whisky"]  # Ejemplo de opciones de bebidas

        combo_box = QComboBox()
        combo_box.addItems(opciones_bebida)
        beb_layout.addWidget(combo_box)

        beb_group_box.setLayout(beb_layout)
        layout.addWidget(beb_group_box)

        return combo_box

    def boton_crear_pedido(self, layout):
        order_button = QPushButton("Realizar pedido")
        order_button.clicked.connect(self.place_order)
        layout.addWidget(order_button)

    def place_order(self):
        comida_seleccionada = self.comida_combo.currentText()
        bebida_seleccionada = self.beb_combo.currentText()
        if comida_seleccionada == "Seleccione su comida" or bebida_seleccionada == "Seleccione su bebida":
            print("Por favor, seleccione su comida y bebida")
        else:
            print(f"Pedido: Comida: {comida_seleccionada}, Bebida: {bebida_seleccionada}")
            self.comida_combo.setCurrentIndex(0)
            self.beb_combo.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MeseroInterfaz()
    ventana.show()
    sys.exit(app.exec())
