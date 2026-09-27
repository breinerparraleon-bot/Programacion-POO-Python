from botella_plastico import BotellaPlastico
from botella_vidrio import BotellaVidrio

mi_botella_plastico = BotellaPlastico(500, "Cilíndrica", "Ergonómico", "Rosca", "Sin grabados", True)

print("DATOS DE LA BOTELLA DE PLÁSTICO")
print("Material:", mi_botella_plastico.get_material())
print(mi_botella_plastico.contener_liquidos(300))
print(mi_botella_plastico.facilitar_vertido())
print(mi_botella_plastico.cierre_hermetico())
print(mi_botella_plastico.transporte())
print(mi_botella_plastico.manejo())
print(mi_botella_plastico.compatibilidad_bebidas())
print(mi_botella_plastico.aplastar())

mi_botella_vidrio = BotellaVidrio(750, "Elegante", "Fino", "Corcho", "Grabado floral", "Ámbar")

print("\nDATOS DE LA BOTELLA DE VIDRIO")
print("Material:", mi_botella_vidrio.get_material())
print(mi_botella_vidrio.contener_liquidos(500))
print(mi_botella_vidrio.facilitar_vertido())
print(mi_botella_vidrio.reutilizacion())
print(mi_botella_vidrio.transparencia())
print(mi_botella_vidrio.esterilizar())