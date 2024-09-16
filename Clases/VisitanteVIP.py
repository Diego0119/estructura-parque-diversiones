from Clases.Visitante import Visitante

class VisitanteVIP(Visitante):
    def __init__(self,nombre,edad,altura,dinero):
        super().__init__(nombre,edad,altura,dinero)

        self.es_vip = True
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero

    
    def beneficios_vip(self):
        print(f"{self.nombre} es un visitante VIP y tiene beneficios especiales.")