class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_habitat(self):
        return self.habitat

    def get_dieta(self):
        return self.dieta

    def get_tamano(self):
        return self.tamano

    def get_color(self):
        return self.color

    def set_edad(self, nueva_edad):
        self.edad = nueva_edad

    def set_habitat(self, nuevo_habitat):
        self.habitat = nuevo_habitat

    def moverse(self):
        return f"El animal {self.nombre} se está desplazando por su hábitat."

    def comunicacion(self):
        return f"El animal {self.nombre} emite sonidos o señales para comunicarse."

    def reproduccion(self):
        return f"El animal {self.nombre} se encuentra en su etapa de reproducción."

    def alimentarse(self):
        return f"El animal {self.nombre} se alimenta de {self.dieta}."

    def adaptacion(self):
        return f"El animal {self.nombre} se adapta al entorno de {self.habitat}."

    def instintos(self):
        return f"El animal {self.nombre} actúa siguiendo sus instintos naturales."

    def descanso(self):
        return f"El animal {self.nombre} está tomando un tiempo de descanso."

    def sueno(self):
        return f"El animal {self.nombre} se encuentra durmiendo."

    def interaccion_social(self):
        return f"El animal {self.nombre} interactúa con otros miembros de su especie."