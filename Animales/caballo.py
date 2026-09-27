from animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, velocidad_maxima=60):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.__velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    def galopar(self):
        return f"El caballo {self.nombre} está galopando a una velocidad de {self.__velocidad_maxima} km/h."    