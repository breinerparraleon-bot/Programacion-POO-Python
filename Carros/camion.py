from carro import Carro

class Camion(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible, capacidad_carga_toneladas=10):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.__capacidad_carga_toneladas = capacidad_carga_toneladas

    def get_capacidad_carga_toneladas(self):
        return self.__capacidad_carga_toneladas

    def levantar_tolva(self):
        return f"El camión ha levantado su tolva para descargar {self.__capacidad_carga_toneladas} toneladas de material."