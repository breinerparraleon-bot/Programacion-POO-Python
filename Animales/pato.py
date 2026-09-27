from animal import Animal

class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipo_vuelo="Migratorio"):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.__tipo_vuelo = tipo_vuelo

    def get_tipo_vuelo(self):
        return self.__tipo_vuelo

    def nadar_y_volar(self):
        return f"El pato {self.nombre} puede nadar y volar con un estilo {self.__tipo_vuelo}."