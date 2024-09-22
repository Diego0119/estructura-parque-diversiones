from Clases.Visitante import Visitante
from Clases.Ticket import Ticket
from Clases.Atraccion import Atraccion
from Clases.Parque import Parque

class VisitanteVIP(Visitante):
    def __init__(self, nombre: str, edad: int, altura: float, dinero: float):
        super().__init__(nombre, edad, altura, dinero)
        
        self._es_vip = True 
        self.contador_atracciones = 0

    def comprar_ticket(self, atraccion: 'Atraccion', parque: 'Parque') -> None:
        if self.contador_atracciones < 2:
            self.contador_atracciones += 1
            print(f"{self.nombre} ha pasado a la atracción sin pagar porque es VIP, se subió a {atraccion.nombre}")
        elif self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio 
            ticket = Ticket(len(parque.ventas) + 1, atraccion.nombre, atraccion.precio, "2024-09-16")
            self.tickets.append(ticket)
            parque.registrar_venta(ticket)
            print(f"{self.nombre} (que es VIP) ha comprado un ticket para la atracción {atraccion.nombre}.")
        else:
            print(f"{self.nombre} no tiene suficiente dinero para comprar un ticket de {atraccion.nombre}.")

    def beneficios_vip(self) -> None:
        print(f"{self.nombre} es un visitante VIP y tiene beneficios especiales.")
