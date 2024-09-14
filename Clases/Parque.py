class Parque:
    def __init__(self,nombre,juegos):
        self.nombre = nombre
        self.juegos = []
        self.contador_tickets = 0;

    def consultar_juegos_activos(self):
        if len(juegos) > 0:
            print(f"Los juegos activos en el parque {self.nombre} son: ")
            for juego in juegos:
                print(f"{juego}")
        else:
            print(f"Ahora mismo no hay juegos activos en {self.nombre}")
        

    def cobrar_ticket(self,visitante,atraccion):
        if atraccion.precio >= visitante.dinero:
            visitante.dinero -=atraccion.precio
            self.contador_tickets+=1;
            ticket = Ticket(self.contador_tickets,atraccion.nombre,atraccion.precio, "Fecha")
            visitante.tickets.append(ticket)
            cobrar_tickets++;
            print(f"Ticket para {atraccion.nombre} vendido a {visitante.nombre}.")
        else:
            print(f"{visitante.nombre} no tiene suficiente dinero para subirse a {atraccion.nombre}")
 