import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, QElapsedTimer, pyqtSignal

class RestaurantInterface(QMainWindow):
    mesa_cambiada = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

        self.initUI()



    def initUI(self):
        self.setWindowTitle('Restaurant Interface')
        self.setGeometry(100, 100, 1000, 800)

        layout = QVBoxLayout()

        self.mesas = []
        self.timers = []

        nombres_mesas = [f'Mesa {i+1}' for i in range(100)]
        x = 50
        y = 50
        button_width = 50
        button_height = 50

        for nombre in nombres_mesas:
            mesa = QPushButton(nombre, self)
            mesa.setGeometry(x, y, button_width, button_height)
            mesa.setStyleSheet("background-color: green")
            mesa.clicked.connect(lambda checked, button=mesa: self.toggle_mesa(button))
            self.mesas.append(mesa)
            self.timers.append(QElapsedTimer())

            x += 70
            if x > 900:
                x = 50
                y += 70

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timers)
        self.timer.start(1000)  # Actualizar cada segundo

    def toggle_mesa(self, mesa):
        index = self.mesas.index(mesa)
        timer = self.timers[index]

        if mesa.styleSheet() == "background-color: green":
            mesa.setStyleSheet("background-color: red")
            timer.start()
            self.mesa_cambiada.emit(mesa.text(), "ocupada")  # Emitir señal con nombre de mesa y estado
        else:
            mesa.setStyleSheet("background-color: green")
            elapsed_time = timer.elapsed()
            elapsed_minutes = elapsed_time // 60000  # Convertir milisegundos a minutos
            if elapsed_minutes >= 60:
                print(f"La mesa {mesa.text()} ha estado ocupada por más de una hora.")
            else:
                print(f"La mesa {mesa.text()} estuvo ocupada durante {elapsed_minutes} minutos.")
            timer.invalidate()  # Reiniciar el temporizador
            self.mesa_cambiada.emit(mesa.text(), "desocupada")  # Emitir señal con nombre de mesa y estado

    def update_timers(self):
        for index, timer in enumerate(self.timers):
            if self.mesas[index].styleSheet() == "background-color: red":
                elapsed_time = timer.elapsed()
                elapsed_minutes = elapsed_time // 60000  # Convertir milisegundos a minutos
                if elapsed_minutes >= 60:
                    print(f"La mesa {self.mesas[index].text()} lleva más de una hora ocupada.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = RestaurantInterface()
    interface.show()
    sys.exit(app.exec())
