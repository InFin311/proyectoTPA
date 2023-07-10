import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QComboBox, QPushButton, QMessageBox, QButtonGroup, QLineEdit, QSpinBox, QCheckBox, QHBoxLayout
from clases import Comanda

class GarzonInterfaz(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.setWindowTitle("Interfaz del Garzón")
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.usuario = usuario
        self.comida_combo = self.crear_seccion_comida(main_layout)
        self.beb_combo = self.crear_seccion_bebestible(main_layout)
        self.mesa_combo = self.crear_seccion_mesa(main_layout)
        self.tipo_combo = self.crear_tipo_comanda(main_layout)

        self.boton_crear_pedido(main_layout)

    def crear_seccion_comida(self, layout):
        comida_group_box = QGroupBox("Comida")
        comida_layout = QVBoxLayout()

        pedido = QLineEdit()

        comida_layout.addWidget(pedido)

        comida_group_box.setLayout(comida_layout)
        layout.addWidget(comida_group_box)

        return pedido

    def crear_seccion_bebestible(self, layout):
        beb_group_box = QGroupBox("Bebestibles")
        beb_layout = QVBoxLayout()

        pedido = QLineEdit()

        beb_layout.addWidget(pedido)

        beb_group_box.setLayout(beb_layout)
        layout.addWidget(beb_group_box)

        return pedido

    def crear_seccion_mesa(self,layout):
        mesas_group_box = QGroupBox("Mesa")
        mesa_layout = QVBoxLayout()

        mesas = QSpinBox()
        mesas.setMinimum(1)
        mesas.setMaximum(100)

        mesa_layout.addWidget(mesas)
        mesas_group_box.setLayout(mesa_layout)
        layout.addWidget(mesas_group_box)

        return mesas
    
    def crear_tipo_comanda(self,layout):
        tipo_group_box = QGroupBox("Tipo de pedido")
        tipo_layout = QHBoxLayout()

        grupo = QButtonGroup()
        tipo1 = QCheckBox("Comida")
        tipo2 = QCheckBox("Bebestible")

        grupo.addButton(tipo1)
        grupo.addButton(tipo2)

        # tipo_layout.addWidget(grupo)
        tipo_layout.addWidget(tipo1)
        tipo_layout.addWidget(tipo2)
        tipo_group_box.setLayout(tipo_layout)
        layout.addWidget(tipo_group_box)
        
        return grupo


    def boton_crear_pedido(self, layout):
        order_button = QPushButton("Realizar pedido")
        order_button.clicked.connect(self.place_order)
        layout.addWidget(order_button)
    

    def place_order(self):
        comida_seleccionada = self.comida_combo.text()
        bebida_seleccionada = self.beb_combo.text()
        mesa_seleccionada = self.mesa_combo.value()
        tipo_seleccionado = self.tipo_combo.checkedButton()

        if tipo_seleccionado.text() == "Comida":
            #guardar en comandas comida
            if comida_seleccionada == "":
                QMessageBox.warning(self, "Advertencia", "Por favor, escriba el pedido")
            else:
                temp_comanda = Comanda(self.usuario, "Comida",mesa_seleccionada)
                temp_comanda.agregar_pedidos(comida_seleccionada)
                temp_comanda.guardar_comanda()
                QMessageBox.information(self, "Pedido realizado", "El pedido fue realizado")

        elif tipo_seleccionado.text() == "Bebestible":
            #guardar comandas bebestible
            if bebida_seleccionada == "":
                QMessageBox.warning(self, "Advertencia", "Por favor, escriba el pedido")
            else:
                temp_comanda = Comanda(self.usuario, "Bebestible",mesa_seleccionada)
                temp_comanda.agregar_pedidos(bebida_seleccionada)
                temp_comanda.guardar_comanda()
                QMessageBox.information(self, "Pedido realizado", "El Pedido fue realizado")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interfaz = GarzonInterfaz("Vicente")
    interfaz.show()
    app.exec()