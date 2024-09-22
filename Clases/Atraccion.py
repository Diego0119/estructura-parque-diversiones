from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Clases.Visitante import Visitante


class Atraccion:
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: str, precio: float):
        self.nombre = nombre
        self.capacidad = capacidad
        self.duracion = duracion
        self.estado = estado
        self.cola: list[Visitante] = []
        self.precio = precio
        self.contador_vip: int = 0

    def iniciar_ronda(self) -> None:
        self.contador_vip = 0 

        for visitante in self.cola:
            if visitante.es_vip:
                self.contador_vip += 1

        if self.contador_vip > len(self.cola) * 0.40:
            print(f"Hay demasiados visitantes VIP en la cola, se eliminará uno.")
            for visitante in self.cola:
                if visitante.es_vip:
                    self.cola.remove(visitante)
                    break

        if self.estado == "activo" and len(self.cola) >= self.capacidad * 0.75:
            self.cola = [] 
            print(f"La atracción {self.nombre} ha empezado a funcionar!!")
        else:
            if self.estado != "activo":
                print("La atracción no está activa.")
            elif len(self.cola) < self.capacidad * 0.75:
                print(f"No hay suficientes visitantes en {self.nombre}.")

    def comenzar_mantenimiento(self) -> None:
        self.estado = "fuera de servicio"
        print(f"La atracción {self.nombre} está ahora en mantenimiento.")
    
    def finalizar_mantenimiento(self) -> None:
        self.estado = "activo"
        print(f"La atracción {self.nombre} ha terminado su mantenimiento y está activa.")

    def verificar_restricciones(self, visitante: 'Visitante') -> bool:
        from Clases.Visitante import Visitante 

        if self.estado != "activo":
            print(f"{self.nombre} no está activa, por lo que {visitante.nombre} no puede subirse.")
            return False
        
        if visitante.altura < 120: 
            print(f"{visitante.nombre} no cumple con la altura mínima para {self.nombre}.")
            return False
        
        if visitante.edad < 12:
            print(f"{visitante.nombre} no cumple con la edad mínima para {self.nombre}.")
            return False

        print(f"{self.nombre} no tiene restricciones, por lo que {visitante.nombre} ha logrado subirse.")
        return True

