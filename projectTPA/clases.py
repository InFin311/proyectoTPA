from datetime import datetime


class Mesa:
    def __init__(self, comandas: list, idMesa=0,
                 nPersonas=1, disponibilidad=True, area="", anfitrion="", estado="", horaReserva=datetime.now()):
        self.idMesa = idMesa
        self.nPersonas = nPersonas
        self.disponibilidad = disponibilidad
        self.area = area
        self.comanda = comandas
        self.anfitrion = anfitrion
        self.estado = estado
        self.horaReserva = horaReserva
        self.horaUso = 0

    def limpiar(self): # cambiar el estado de la mesa a "disponible", además de mandar a un runner para limpiar la mesa
        pass

    def servir(self): # Mandar runners para servir a las mesas
        pass

    def reservar(self): # Asignar anfitrion
        pass

    def pago(self): # Sistema de pago
        pass

    def __str__(self):
        horaReserva = self.horaReserva.strftime("%H")
        minutoReserva = self.horaReserva.strftime("%M")

        return f"En la mesa {self.idMesa+1}, la reserva está para las {horaReserva}:{minutoReserva}"


class Comanda:
    def __init__(self):
        pass


class Plato:
    def __init__(self):
        pass


if __name__ == "__main__":
    _time = datetime.now()
    mesita = Mesa([Comanda()], horaReserva=_time)
    print(mesita)
