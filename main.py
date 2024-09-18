from Clases.Atraccion import Atraccion
from Clases.AtraccionInfantil import AtraccionInfantil
from Clases.MontanaRusa import MontanaRusa
from Clases.Parque import Parque
from Clases.Ticket import Ticket
from Clases.Visitante import Visitante
from Clases.VisitanteVIP import VisitanteVIP

# visitantes
visitante_1 = Visitante("Diego", 21, 170, 24000)
visitante_2 = Visitante("Maite", 20, 165, 18000)
visitante_3 = Visitante("Carla", 20, 165, 18000)
visitante_4 = Visitante("Sofia", 20, 165, 18000)
visitante_5 = Visitante("Humberto", 20, 165, 18000)
visitante_6 = Visitante("Jose", 20, 165, 18000)
visitante_7 = Visitante("Matilda", 9, 130,5000)
visitante_vip = VisitanteVIP("Carlos", 25, 180, 30000)

# atracciones
atraccion_1 = Atraccion("Boomerang", 4, 3, "activo", 1000)
atraccion_infantil = AtraccionInfantil("Carrusel", 10, 5, "activo", 500)
montana_rusa = MontanaRusa("Montaña Rusa Extrema", 4, 2, "activo", 1500, 120, 60, 1000)

# parque
parque = Parque("Diversiones Feliz", [atraccion_1, atraccion_infantil, montana_rusa])
print("\nLos juegos activos son:")
parque.consultar_juegos_activos()

# compras de tickets
print("\nCompra de Tickets:")
visitante_1.comprar_ticket(atraccion_1,parque)
visitante_2.comprar_ticket(montana_rusa,parque)
visitante_3.comprar_ticket(atraccion_1,parque)
visitante_4.comprar_ticket(montana_rusa,parque)
visitante_5.comprar_ticket(atraccion_1,parque)
visitante_6.comprar_ticket(montana_rusa,parque)
visitante_7.comprar_ticket(atraccion_infantil,parque)
visitante_vip.comprar_ticket(montana_rusa,parque)

print("\nCobrar tickets para que se puedan subir:")
parque.cobrar_ticket(visitante_1, atraccion_infantil)
parque.cobrar_ticket(visitante_2, montana_rusa)
parque.cobrar_ticket(visitante_vip, montana_rusa)
parque.cobrar_ticket(visitante_3, atraccion_1)
parque.cobrar_ticket(visitante_4, montana_rusa)
parque.cobrar_ticket(visitante_5, atraccion_1)
parque.cobrar_ticket(visitante_6, montana_rusa)
parque.cobrar_ticket(visitante_7,atraccion_infantil)

# # visitantes haciendo cola
print("\nVisitantes en la cola:")
visitante_1.hacer_cola(atraccion_infantil)
visitante_2.hacer_cola(montana_rusa)
visitante_vip.hacer_cola(montana_rusa)
visitante_3.hacer_cola(atraccion_1)
visitante_4.hacer_cola(montana_rusa)
visitante_5.hacer_cola(atraccion_1)
visitante_6.hacer_cola(montana_rusa)
visitante_7.hacer_cola(atraccion_infantil)

# ronda de atracciones
print("\nIniciar Rondas:")
atraccion_1.iniciar_ronda()
montana_rusa.iniciar_ronda()
atraccion_infantil.iniciar_ronda()

# mantenimiento
print("\nMantenimiento:")
atraccion_1.comenzar_mantenimiento()
atraccion_1.finalizar_mantenimiento()

# ventas
print("\nResumen de ventas:")
parque.resumen_de_ventas("2024-09-16")
