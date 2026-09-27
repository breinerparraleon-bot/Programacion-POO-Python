from deportivo import Deportivo
from camion import Camion

print("EJEMPLO 1: CARRO DEPORTIVO")
mi_deportivo = Deportivo("Nissan GT-R (R35)", "Negro", "V6 Turbo", 2, 2, "Gasolina", True)
print("Modelo:", mi_deportivo.get_modelo())
print("Color:", mi_deportivo.get_color())
print("Motor:", mi_deportivo.get_motor())
print(mi_deportivo.arranque())
print(mi_deportivo.aceleracion_y_frenado())
print(mi_deportivo.climatizacion())
print(mi_deportivo.activar_turbo())
print(mi_deportivo.apagado())

print("\nEJEMPLO 2: CAMIÓN DE CARGA")
mi_camion = Camion("Mack Titan", "Blanco", "Diesel 13L", 2, 3, "ACPM", 15)
print("Modelo:", mi_camion.get_modelo())
print("Tipo de Combustible:", mi_camion.get_tipo_combustible())
print("Capacidad de Pasajeros:", mi_camion.get_capacidad_pasajeros())
print(mi_camion.arranque())
print(mi_camion.sistema_direccion())
print(mi_camion.tipo_seguridad())
print(mi_camion.levantar_tolva())
print(mi_camion.apagado())