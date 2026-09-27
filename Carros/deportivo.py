from carro import Carro

class Deportivo(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible, modo_carrera=True):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.__modo_carrera = modo_carrera

    def get_modo_carrera(self):
        return self.__modo_carrera

    def activar_turbo(self):
        if self.__modo_carrera:
            return "¡Modo turbo activado en el carro deportivo! Máxima potencia de aceleración."
        return "El modo carrera está desactivado."