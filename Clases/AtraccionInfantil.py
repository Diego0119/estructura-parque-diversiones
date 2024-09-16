from Clases.Atraccion import Atraccion

class AtraccionInfantil(Atraccion):
    def __init__(self, nombre, capacidad, duracion, estado, precio):
        super().__init__(nombre, capacidad, duracion, estado, precio)
    
    def verificar_restricciones(self, visitante):
        if visitante.edad <= 10:
            print(f"{visitante.nombre} puede acceder a la atracción infantil {self.nombre}.")
        else:
            print(f"{visitante.nombre} no cumple con las restricciones de edad para la atracción infantil {self.nombre}.")
            