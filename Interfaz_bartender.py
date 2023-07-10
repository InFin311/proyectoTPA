import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QVBoxLayout, QWidget, QHBoxLayout, QTableWidgetItem, QPushButton, QHeaderView
from PyQt6.QtCore import QTimer
from datetime import datetime
import pandas as pd
import os

class VentanaBartender(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.setWindowTitle("Bartender")
        self.usuario_actual = usuario
        self.setFixedWidth(600)
        #Elementos

        bienvenida = QLabel(f"Bienvenido {self.usuario_actual}")
        titulo = QLabel("Comandas actuales")
        self.tabla = QTableWidget(100,5)
        self.hora_actual = QLabel(f"Hora actual: {datetime.now().strftime('%H:%M:%S')}")

        actualizar = QPushButton("Actualizar")
        actualizar.clicked.connect(self.imprimir_comandas)
        
        self.boton_cambiar_estado = QPushButton("Cambiar estado")

        self.fila_seleccionada = 0

        #Config
        self.tabla.setHorizontalHeaderLabels(["Mesa","Garzon","Hora","Pedidos","Estado"])
        self.tabla.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.tabla.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeMode.ResizeToContents)
        self.tabla.cellClicked.connect(self.actualizar_fila_seleccionada)
        self.boton_cambiar_estado.clicked.connect(self.cambiar_estado)
        #Layouts
        #Hora y titulo
        hora_titulo = QHBoxLayout()
        hora_titulo.addWidget(titulo)
        hora_titulo.addWidget(self.hora_actual)
        hora_titulo.addWidget(actualizar)
        hora_titulo.addWidget(self.boton_cambiar_estado)

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
    
    def imprimir_comandas(self):
        archivo = open(f"{os.path.dirname(__file__)}/data/comandas_bebestibles.csv", "r")
        temp_dataframe = pd.read_csv(archivo, names=["Mesa","Garzon","Hora","Pedidos","Estado"])
        archivo.close()
        if len(temp_dataframe) == 0:
            #Si el dataframe esta vacio
            pass
        else:
            #Si el dataframe no esta vacio
            #Entrega la cantidad de filas que tiene el dataframe
            filas_dataframe = temp_dataframe.shape[0]
            columnas_dataframe = len(temp_dataframe.columns)
            for i in range(filas_dataframe):
                for j in range(columnas_dataframe):
                    self.tabla.setItem(i,j,QTableWidgetItem(f"{temp_dataframe.iloc[i][j]}"))
    
    #Esta funcion avisa de que pueden existir nuevas comandas
    def actualizar_fila_seleccionada(self, fila):
        self.fila_seleccionada = fila
        
    def cambiar_estado(self):
        archivo = open(f"{os.path.dirname(__file__)}/data/comandas_bebestibles.csv", "r")
        archivo_leido = archivo.readlines()
        archivo.close()
        if "En espera" in archivo_leido[self.fila_seleccionada]:
            archivo_leido[self.fila_seleccionada] = archivo_leido[self.fila_seleccionada].replace("En espera", "Preparando")
        elif "Preparando" in archivo_leido[self.fila_seleccionada]:
            archivo_leido[self.fila_seleccionada] = archivo_leido[self.fila_seleccionada].replace("Preparando", "Terminado")
        elif "Terminado" in archivo_leido[self.fila_seleccionada]:
            archivo_leido[self.fila_seleccionada] = archivo_leido[self.fila_seleccionada].replace("Terminado", "En espera")

        contenido_reemplazado = ""
        for elemento in archivo_leido:
            contenido_reemplazado += elemento
        
        archivo = open(f"{os.path.dirname(__file__)}/data/comandas_bebestibles.csv", "w")
        archivo.write(contenido_reemplazado)
        archivo.close()
        self.imprimir_comandas()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaBartender("Vicente")
    window.show()
    app.exec()
