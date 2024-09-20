from Clases.Visitante import Visitante
from Clases.Ticket import Ticket

class VisitanteVIP(Visitante):
    def __init__(self,nombre,edad,altura,dinero):
        super().__init__(nombre,edad,altura,dinero)

        self.es_vip = True
        self.contador_atracciones = 0
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = []

    def comprar_ticket(self,atraccion, parque):
        if self.contador_atracciones < 2:
            self.contador_atracciones =+1
            ticket = Ticket(len(parque.ventas) + 1, atraccion.nombre, atraccion.precio, "2024-09-16")
            self.tickets.append(ticket)
            parque.registrar_venta(ticket)
            print(f"{self.nombre} ha pasado a la atracción sin pagar porque es vip, se subió a {atraccion.nombre}")
        elif self.dinero >= atraccion.precio:
            self.dinero =- atraccion.precio
            ticket = Ticket(len(parque.ventas) + 1, atraccion.nombre, atraccion.precio, "2024-09-16")
            self.tickets.append(ticket)
            parque.registrar_venta(ticket)
            print(f"{self.nombre} (que es vip) ha comprado un ticket para la atraccion {atraccion.nombre}")
            
    
    
    def beneficios_vip(self):
        print(f"{self.nombre} es un visitante VIP y tiene beneficios especiales.")