from Clases.Ticket import Ticket

class Visitante:
    def __init__(self,nombre,edad,altura,dinero):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = []
        self.cola  = []

    def comprar_ticket(self, atraccion,parque):
        if self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio
            ticket = Ticket(len(parque.ventas) + 1, atraccion.nombre, atraccion.precio, "2024-09-16")
            self.tickets.append(ticket)
            parque.registrar_venta(ticket)
            print(f"{self.nombre} ha comprado un ticket para la atraccion {atraccion.nombre}")
        else:
            print(f"{self.nombre} no tiene suficiente dinero para comprar un ticket de {atraccion.nombre}")


    def entregar_ticket(self,atraccion):
        for ticket in self.tickets:
            if ticket.atraccion.nombre == atraccion.nombre:
                self.tickets.remove(ticket)
                printf(f"{self.nombre} entrego el ticket para la atraccion {ticket.atraccion}")
                return
        print(f"{self.nombre} no tiene un ticket para la atraccion {ticket.atraccion}")


    def hacer_cola(self, atraccion):
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
