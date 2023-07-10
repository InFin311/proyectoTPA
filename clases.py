from datetime import datetime
import os

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
    def __init__(self,garzon: str, tipo:str, mesa:int):
        self.garzon = garzon.lower()
        self.hora = datetime.now().strftime("%H:%M")
        self.pedidos = []
        #estados si es comida 0 = en espera ; 1 = preparando; 2 = cocinando; 3 = terminado
        #estados si es bebestible 0 = en espera ; 1 = preparando; 2 = terminado
        self.estado = 0
        self.tipo = tipo.lower()
        self.mesa = mesa

    def pedido_vacio(self):
        if len(self.pedidos) == 0:
            return True
        else:
            return False
    def agregar_pedidos(self,pedido:str):
        self.pedidos.append(pedido)

    def eliminar_pedidos(self,pedido:str):
        if self.pedido_vacio == True:
            #Retorno false porque no puedo eliminar un pedido en una lista vacia
            return False
        else:
            try:
                self.pedido_vacio.remove(pedido)
                return True
            except ValueError:
                return False
    
    def cambiar_estado(self,nuevo_estado:int):
        self.estado = nuevo_estado

        return True
    
    def get_estado(self):
        if self.get_tipo() == "comida":
            if self.estado == 0:
                return "En espera"
        
            elif self.estado == 1:
                return "Preparando"
        
            elif self.estado == 2:
                return "Cocinando"
        
            elif self.estado == 3:
                return "Terminado"
            
        elif self.get_tipo() == "bebestible":
            if self.estado == 0:
                return "En espera"
            elif self.estado == 1:
                return "Preparando"
            elif self.estado == 2:
                return "Terminado"

    def get_garzon(self):
        return self.garzon
    
    def get_hora(self):
        return self.hora
    
    def get_pedidos(self):
        if self.pedido_vacio == True:
            return "El pedido esta vacio"
        else:
            aux = ""
            for i in self.pedidos:
                if len(self.pedidos) == 1:
                    aux += f"{i}"
                else:
                    #Si el elemento es el ultimo
                    if i == self.pedidos[-1]:
                        aux += f"{i}"
                    else:
                        aux += f"{i} - "
            return aux
    def get_tipo(self):
        return self.tipo
    
    def get_mesa(self):
        return self.mesa
    
    def guardar_comanda(self):
        if self.pedido_vacio == True:
            #Retorna falso, no se guardaran pedidos vacios
            return False
        else:
            if self.get_tipo() == "comida":
                archivo = open(f"{os.path.dirname(__file__)}/data/comandas_comida.csv","a")
                temp_comanda = f"{self.get_mesa()},{self.get_garzon()},{self.get_hora()},{self.get_pedidos()},{self.get_estado()}\n"
                archivo.write(temp_comanda)
                archivo.close()
                return True
            elif self.get_tipo() == "bebestible":
                archivo = open(f"{os.path.dirname(__file__)}/data/comandas_bebestibles.csv","a")
                temp_comanda = f"{self.get_mesa()},{self.get_garzon()},{self.get_hora()},{self.get_pedidos()},{self.get_estado()}\n"
                archivo.write(temp_comanda)
                archivo.close()
                return True
        



class Plato:
    def __init__(self):
        pass


if __name__ == "__main__":
    comandafalsa = Comanda("Vicente","Comida",1)
    comandafalsa.agregar_pedidos("hamburguesa")
    comandafalsa.agregar_pedidos("papas")
    comandafalsa.guardar_comanda()
    comandafalsa = Comanda("Yo", "Bebestible",1)
    comandafalsa.agregar_pedidos("bebida")
    comandafalsa.agregar_pedidos("agua")
    comandafalsa.agregar_pedidos("jugo")
    comandafalsa.guardar_comanda()
