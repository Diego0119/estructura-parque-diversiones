from Clases.Atraccion import Atraccion
from Clases.Visitante import Visitante

class AtraccionInfantil(Atraccion):
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: str, precio: float):
        super().__init__(nombre, capacidad, duracion, estado, precio)
    
    def verificar_restricciones(self, visitante: Visitante) -> bool: 
        if visitante.edad <= 10:
            print(f"{visitante.nombre} puede acceder a la atracción infantil {self.nombre}.")
            return True
        else:
            print(f"{visitante.nombre} no cumple con las restricciones de edad para la atracción infantil {self.nombre}.")
            return False
