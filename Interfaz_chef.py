import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, \
    QComboBox, QDialog, QMessageBox, QListWidget, QLayout
from PyQt6.QtGui import QColor
from clases import Comanda


class verComanda(QDialog):
    def __init__(self, comandas: list, main_win: QMainWindow):
        super().__init__()

        self.comandas = comandas
        self.main_window = main_win

        self.setWindowTitle(f"Comanda de {self.comandas[0]}")
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout()
        botones = QHBoxLayout()
        self.setLayout(main_layout)

        botones.addWidget(QPushButton("Guardar"))
        botones.itemAt(0).widget().clicked.connect(self.guardarNuevaComanda)
        botones.addWidget(QPushButton("Cancelar"))
        botones.itemAt(1).widget().clicked.connect(self.hide)

        main_layout.addWidget(QLabel("Garzon:"))
        main_layout.addWidget(QLineEdit(f"{self.comandas[0]}"))
        main_layout.addWidget(QLabel("Hora:"))
        main_layout.addWidget(QLineEdit(f"{self.comandas[1]}"))
        main_layout.addWidget(QLabel("Pedidos:"))
        main_layout.addWidget(QLineEdit(f"{self.comandas[2]}"))
        main_layout.addWidget(QLabel("Estado:"))
        main_layout.addWidget(QLineEdit(f"{self.comandas[3]}"))
        main_layout.addLayout(botones)

        self.widgets = ChefUI.getWidgets(main_layout)

    def guardarNuevaComanda(self):
        archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv", "r")
        comandas = archivo.readlines()
        aux = 0
        for i in comandas:
            if self.comandas[0] in i:
                aux = comandas.index(i)
                break
        archivo.close()

        archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv", "w")

        res = []
        for widget in self.widgets:
            if type(widget) is QLineEdit:
                res += [widget.text()]

        if not ("\n" in res[-1]):
            res[-1] = res[-1] + "\n"

        res = ",".join(res)
        comandas.pop(aux)

        comandas.insert(aux, res)
        archivo.writelines(comandas)

        # update main window
        self.main_window.column.clear()
        try:
            archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv", "r")
            comandas = archivo.readlines()
            for i in comandas:
                i = i.replace(",", ", ")
                self.main_window.column.addItem(i)

            archivo.close()
        except FileExistsError:
            pass

        archivo.close()

        self.hide()


class ChefUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chef Menu")
        self.setGeometry(700, 400, 400, 200)

        self.comanda = None
        self.comanda_ventana = None

        self.main_layout = QHBoxLayout()
        self.section1 = QVBoxLayout()
        self.section1.addWidget(QLabel("Menu de chef"))
        self.section1.addWidget(QLabel("Haz doble click para editar"))

        self.main_layout.addLayout(self.section1)

        self.setLayout(self.main_layout)
        self.column = QListWidget()

        try:
            archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv", "r")
            comandas = archivo.readlines()
            for i in comandas:
                i = i.replace(",", ", ")
                self.column.addItem(i)

            archivo.close()
        except FileExistsError:
            pass

        self.column.doubleClicked.connect(self.abrirComanda)
        self.main_layout.addWidget(self.column)

        self.main_objects = self.getWidgets(self.main_layout, True)
        self.section1_objects = self.getWidgets(self.section1)

        for i in self.main_objects:
            if type(i) is not QLabel and type(i) is not QVBoxLayout:
                i.setStyleSheet(f"background-color: {QColor(70, 70, 70).name()}; color: white")

        self.setStyleSheet(f"background-color: {QColor(50, 50, 50).name()}; color: white")

        center = QWidget()
        center.setLayout(self.main_layout)
        self.setCentralWidget(center)

    def abrirComanda(self):
        comanda_texto = self.column.selectedItems()[0].text()
        comanda_texto = comanda_texto.split(", ")

        self.comanda_ventana = verComanda(comanda_texto, self)
        self.comanda_ventana.setStyleSheet(f"background-color: {QColor(50, 50, 50).name()}; color: white")
        self.comanda_ventana.show()

    def actualizarLista(self, col: QListWidget):
        try:
            archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv", "r")
            comandas = archivo.readlines()
            for i in comandas:
                i = i.replace(",", ", ")
                col.addItem(i)

            archivo.close()
        except FileExistsError:
            pass

        self.update()

    @staticmethod
    def getWidgets(a0: QLayout, all=False):
        index = a0.count() - 1
        res = []
        while index >= 0:
            myWidget = a0.itemAt(index).widget()
            myLayout = a0.itemAt(index).layout()
            if myLayout is not None and all:
                res += [myLayout]
            elif myWidget is not None:
                res += [myWidget]

            index -= 1
        res.reverse()
        return res


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChefUI()
    win.show()
    sys.exit(app.exec())
