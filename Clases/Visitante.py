from typing import TYPE_CHECKING
from Clases.Ticket import Ticket

if TYPE_CHECKING:
    from Clases.Atraccion import Atraccion
    from Clases.Parque import Parque


class Visitante:
    def __init__(self, nombre: str, edad: int, altura: float, dinero: float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets: list[Ticket] = [] 
        self.cola: list[None] = [] 
        self._es_vip = False 

    def comprar_ticket(self, atraccion: 'Atraccion', parque: 'Parque') -> None:
        if self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio
            ticket = Ticket(len(parque.ventas) + 1, atraccion.nombre, atraccion.precio, "2024-09-16")
            self.tickets.append(ticket)
            parque.registrar_venta(ticket)
            print(f"{self.nombre} ha comprado un ticket para la atracción {atraccion.nombre}.")
        else:
            print(f"{self.nombre} no tiene suficiente dinero para comprar un ticket de {atraccion.nombre}.")

    def entregar_ticket(self, atraccion: 'Atraccion') -> None:
        for ticket in self.tickets:
            if ticket.atraccion == atraccion.nombre:
                self.tickets.remove(ticket)
                print(f"{self.nombre} entregó el ticket para la atracción {ticket.atraccion}.")
                return
        print(f"{self.nombre} no tiene un ticket para la atracción {atraccion.nombre}.")

    def hacer_cola(self, atraccion: 'Atraccion') -> None:
        cumple_restricciones = atraccion.verificar_restricciones(self)
        
        if not cumple_restricciones:
            print(f"{self.nombre} no puede acceder a la atracción {atraccion.nombre}.")
            return

        if atraccion.estado == "activo":
            if self not in atraccion.cola:
                atraccion.cola.append(self)
                print(f"{self.nombre} se ha puesto en la cola de {atraccion.nombre}.")
            else:
                print(f"{self.nombre} ya está en la cola de {atraccion.nombre}.")
        else:
            print(f"La atracción {atraccion.nombre} no está activa.")

    @property
    def es_vip(self) -> bool:
        return self._es_vip
