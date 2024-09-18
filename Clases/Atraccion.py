class Atraccion:
    def __init__(self, nombre, capacidad, duracion, estado, precio):
        self.nombre = nombre
        self.capacidad = capacidad
        self.duracion = duracion
        self.estado = estado
        self.cola = []
        self.precio = precio

    def iniciar_ronda(self):
        if self.estado == "activo" and len(self.cola) >= self.capacidad * 0.75:
            self.cola = []
            print(f"La atraccion {self.nombre} ha empezado a funcionar!!")
        else:
            if self.estado != "activo":
                print("La atraccion no esta activa")
            elif len(self.cola) < self.capacidad * 0.75:
                print(f"No hay suficientes visitantes en {self.nombre}")


    def comenzar_mantenimiento(self):
        self.estado = "fuera de servicio"
        print(f"La atracción {self.nombre} está ahora en mantenimiento.")
    
    def finalizar_mantenimiento(self):
        self.estado = "activo"
        print(f"La atracción {self.nombre} ha terminado su mantenimiento y está activa.")

    def verificar_restricciones(self,visitante):
        print(f"{self.nombre} no tiene restricciones, por lo que {visitante.nombre} ha logrado subirse")