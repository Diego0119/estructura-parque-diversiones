from Clases.Ticket import Ticket

class Parque:
    def __init__(self,nombre,juegos):
        self.nombre = nombre
        self.juegos = []
        self.contador_tickets = 0;
        self.ventas = []

    def registrar_venta(self, ticket):
        self.ventas.append(ticket)

    def resumen_de_ventas(self, dia):
        resumen = {}
        total_ingresos = 0

        for ticket in self.ventas:
            if ticket.fecha_compra == dia:
                if ticket.atraccion in resumen:
                    resumen[ticket.atraccion]['cantidad'] += 1
                    resumen[ticket.atraccion]['ingresos'] += ticket.precio
                else:
                    resumen[ticket.atraccion] = {'cantidad': 1, 'ingresos': ticket.precio}
                total_ingresos += ticket.precio
        
        for atraccion, data in resumen.items():
            print(f"Atracción: {atraccion}, Tickets vendidos: {data['cantidad']}, Ingresos: ${data['ingresos']}")
        print(f"Total de ingresos del día: ${total_ingresos}")

    def consultar_juegos_activos(self):
        if len(self.juegos) > 0:
            print(f"Los juegos activos en el parque {self.nombre} son: ")
            for juego in self.juegos:
                print(f"{juego}")
        else:
            print(f"Ahora mismo no hay juegos activos en {self.nombre}")
        

    def cobrar_ticket(self, visitante, atraccion):
        ticket_encontrado = False

        for ticket in visitante.tickets:
            if ticket.atraccion == atraccion.nombre:
                ticket_encontrado = True
                visitante.tickets.remove(ticket) 
                print(f"Ticket para {atraccion.nombre} cobrado a {visitante.nombre}.")
                break
        
        if not ticket_encontrado:
            print(f"{visitante.nombre} no tiene un ticket válido para {atraccion.nombre}.")