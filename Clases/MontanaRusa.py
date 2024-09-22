from Clases.Atraccion import Atraccion
from Clases.Visitante import Visitante

class MontanaRusa(Atraccion):
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: str, precio: int, velocidad_maxima: int, altura_maxima: int, extension: int):
        super().__init__(nombre, capacidad, duracion, estado, precio)
        
        self.velocidad_maxima = velocidad_maxima 
        self.altura_maxima = altura_maxima  
        self.extension = extension  

    def verificar_restricciones(self, visitante: Visitante) -> bool:
        if visitante.altura >= 140:
            print(f"{visitante.nombre} cumple con las restricciones de altura para la Montaña Rusa {self.nombre}.")
            return True
        else:
            print(f"{visitante.nombre} no tiene la altura mínima requerida para subirse a la Montaña Rusa {self.nombre}.")
            return False
