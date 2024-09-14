class Visitante:
    def __init__(self,nombre,edad,altura,dinero):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = []

    def comprar_ticket(self, atraccion):
        if self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio
            ticket = Ticket(atraccion.nombre,atraccion.precio)
            self.tickets.append(ticket)
            printf(f"{self.nombre} ha comprado un ticket para la atraccion {atraccion.nombre}")
        else:
            printf(f"{self.nombre} no tiene suficiente dinero para comprar un ticket de {atraccion.nombre}")


    def entregar_ticket(self,atraccion):
        for ticket in self.tickets:
            if ticket.atraccion.nombre == atraccion.nombre:
                self.tickets.remove(ticket)
                printf(f"{self.nombre} entrego el ticket para la atraccion {ticket.atraccion}")
                return
        printf(f"{self.nombre} no tiene un ticket para la atraccion {ticket.atraccion}")


    def hacer_cola(self,atraccion):
        pass