class Ticket:
    def __init__(self,numero,atraccion,precio,fecha_compra):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = fecha_compra
        self.ventas = []

    def añadir_ticket(self, nombre_atraccion, precio_atraccion):
        self.ventas.append({
            "nombre_atraccion": nombre_atraccion,
            "precio_atraccion": precio_atraccion
        })