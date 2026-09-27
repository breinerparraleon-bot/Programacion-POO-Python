class Carro:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_motor(self):
        return self.motor

    def get_numero_puertas(self):
        return self.numero_puertas

    def get_capacidad_pasajeros(self):
        return self.capacidad_pasajeros

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def set_motor(self, nuevo_motor):
        self.motor = nuevo_motor

    def arranque(self):
        return f"El carro modelo {self.modelo} ha encendido el motor {self.motor}."

    def apagado(self):
        return f"El carro modelo {self.modelo} se ha apagado correctamente."

    def aceleracion_y_frenado(self):
        return "El vehículo está acelerando y aplicando el sistema de frenado."

    def sistema_direccion(self):
        return "El sistema de dirección responde con precisión al volante."

    def climatizacion(self):
        return "El sistema de aire acondicionado y climatización está activo."

    def tipo_seguridad(self):
        return "Equipado con sistemas de seguridad activa y pasiva."

    def luces(self):
        return "Las luces delanteras, traseras y direccionales están encendidas."

    def sistema_ventanas(self):
        return "Accionando el sistema de ventanas eléctricas."

    def sistema_espejo(self):
        return "Ajustando los espejos retrovisores de forma electrónica."