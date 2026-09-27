from caballo import Caballo
from pato import Pato

print("EJEMPLO 1: CABALLO")
mi_caballo = Caballo("Juan", 5, "Pradera", "Hierba y grano", "Grande", "Marrón", 65)
print("Nombre:", mi_caballo.get_nombre())
print("Edad:", mi_caballo.get_edad(), "años")
print("Hábitat:", mi_caballo.get_habitat())
print(mi_caballo.alimentarse())
print(mi_caballo.moverse())
print(mi_caballo.galopar())
print(mi_caballo.descanso())

print("\nEJEMPLO 2: PATO")
mi_pato = Pato("Lucas", 2, "Laguna", "Peces pequeños y plantas", "Pequeño", "Verde y blanco", "Corto")
print("Nombre:", mi_pato.get_nombre())
print("Color:", mi_pato.get_color())
print("Dieta:", mi_pato.get_dieta())
print(mi_pato.comunicacion())
print(mi_pato.adaptacion())
print(mi_pato.nadar_y_volar())
print(mi_pato.sueno())