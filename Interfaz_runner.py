from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt
import os

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

        # self.boton_limpiar = QPushButton("Limpiar Mesa")
        # self.boton_limpiar.clicked.connect(self.limpiar_mesa)
        # self.layout.addWidget(self.boton_limpiar)

        self.boton_actualizar = QPushButton("Actualizar")
        self.boton_actualizar.clicked.connect(self.actualizar_mesas)
        self.layout.addWidget(self.boton_actualizar)

        # self.simular_eventos()  # Simulación de eventos

    def simular_eventos(self):
        # Ejemplos de mesas que requieren servicios
        self.lista_mesas.addItem("Mesa 1")
        self.lista_mesas.addItem("Mesa 2")
        self.lista_mesas.addItem("Mesa 3")

        # Ejemplos de comandas listas para servir
        self.comandas_listas = ["Comanda 1", "Comanda 2"]

    def actualizar_mesas(self):
        archivo_bebestibles = open(f"{os.path.dirname(__file__)}/data/comandas_bebestibles.csv","r")
        archivo_comida = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv","r")

        for linea in archivo_bebestibles:
            if "Terminado" in linea:
                aux = linea.split(",")
                comanda = f"Mesa {aux[0]}, Pedido: {aux[3]}, Bebestible"
                posibles = self.lista_mesas.findItems(comanda, Qt.MatchFlag.MatchExactly)
                try:
                    if posibles[0].text() == comanda:
                        continue
                    else:
                        self.lista_mesas.addItem(comanda)
                except:
                    self.lista_mesas.addItem(comanda)
        for linea in archivo_comida:
            if "Terminado" in linea:
                aux = linea.split(",")
                comanda = f"Mesa {aux[0]}, Pedido: {aux[3]}, Comida"
                posibles = self.lista_mesas.findItems(comanda, Qt.MatchFlag.MatchExactly)
                try:
                    if posibles[0].text() == comanda:
                        continue
                    else:
                        self.lista_mesas.addItem(comanda)
                except:
                    self.lista_mesas.addItem(comanda)
        archivo_bebestibles.close()
        archivo_comida.close()
        

    #Una vez que es servido eliminar la comanda del archivo        
    def servir_mesa(self):  # Realizar acciones para servir la mesa según el número de mesa seleccionado
        mesa_seleccionada = self.lista_mesas.currentItem().text()
        mesa_seleccionada = mesa_seleccionada.split(",")
        #tipo mesa_seleccionada[2]
        #mesa mesa_seleccionada[0][4:6]

        if "Bebestible" in mesa_seleccionada[2]:
            #trabajar en archivo bebestibles
            archivo = open(f"{os.path.dirname(__file__)}/data/comandas_bebestibles.csv","r")
            mesa = mesa_seleccionada[0][5:6]
            archivo_editado = str()
            for linea in archivo:
                if linea[0] == mesa:
                    continue
                else:
                    archivo_editado += linea
            archivo.close()
            archivo = open(f"{os.path.dirname(__file__)}/data/comandas_bebestibles.csv","w")
            archivo.write(archivo_editado)
            archivo.close()
            

            self.mostrar_dialogo_informativo(f"Sirviendo mesa {mesa}")
            self.lista_mesas.takeItem(self.lista_mesas.currentRow())

        elif "Comida" in mesa_seleccionada[2]:
            #trabajar en archivo comida
            archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv","w")
            mesa = mesa_seleccionada[0][5:6]
            archivo_editado = str()
            for linea in archivo:
                if linea[0] == mesa:
                    continue
                else:
                    archivo_editado += linea
            print(archivo_editado)
            archivo.close()
            archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv","w")
            archivo.write(archivo_editado)
            archivo.close()
            
            
            self.mostrar_dialogo_informativo(f"Sirviendo mesa {mesa}")
            self.lista_mesas.takeItem(self.lista_mesas.currentRow())
            
    def limpiar_mesa(self):  # Realizar acciones para limpiar la mesa según el número de mesa seleccionado
        mesa_seleccionada = self.lista_mesas.currentItem()
        if mesa_seleccionada:
            numero_mesa = mesa_seleccionada.text()
            self.mostrar_dialogo_informativo(f"Limpiando {numero_mesa}")
            self.lista_mesas.takeItem(self.lista_mesas.currentRow())
            self.mostrar_dialogo_informativo(f"{numero_mesa} liberada y lista para nuevos comensales")

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


