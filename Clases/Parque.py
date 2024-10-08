from Clases.Ticket import Ticket
from Clases.Atraccion import Atraccion
from Clases.Visitante import Visitante

class Parque:
    def __init__(self, nombre: str, juegos: list[Atraccion]): 
        self.nombre = nombre
        self.juegos = juegos
        self.contador_tickets = 0
        self.ventas: list[Ticket] = []

    def registrar_venta(self, ticket: Ticket) -> None: 
        self.ventas.append(ticket)

    def resumen_de_ventas(self, dia: str) -> None:
        resumen: dict[str, dict[str, float]] = {}
        total_ingresos: float = 0.0

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

    def consultar_juegos_activos(self) -> None: 
        if len(self.juegos) > 0:
            print(f"Los juegos activos en el parque {self.nombre} son: ")
            for juego in self.juegos:
                print(f"{juego.nombre}")
        else:
            print(f"Ahora mismo no hay juegos activos en {self.nombre}")

    def cobrar_ticket(self, visitante: Visitante, atraccion: Atraccion) -> None:
        ticket_encontrado = False

        for ticket in visitante.tickets:
            if ticket.atraccion == atraccion.nombre:
                ticket_encontrado = True
                visitante.tickets.remove(ticket) 
                print(f"Ticket para {atraccion.nombre} cobrado a {visitante.nombre}.")
                break
        
        if not ticket_encontrado:
            print(f"{visitante.nombre} no tiene un ticket válido para {atraccion.nombre}.")
