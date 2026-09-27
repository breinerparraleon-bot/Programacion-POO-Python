class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def get_material(self):
        return self.material

    def get_capacidad(self):
        return self.capacidad

    def get_forma(self):
        return self.forma

    def get_diseno(self):
        return self.diseno

    def get_tapa(self):
        return self.tapa

    def get_grabados(self):
        return self.grabados

    def set_capacidad(self, nueva_capacidad):
        self.capacidad = nueva_capacidad

    def set_diseno(self, nuevo_diseno):
        self.diseno = nuevo_diseno

    def contener_liquidos(self, cantidad):
        return f"Conteniendo {cantidad} ml de líquido de forma segura."

    def facilitar_vertido(self):
        return "Facilitando el vertido del contenido gracias a su diseño."

    def cierre_hermetico(self):
        return f"Cierre hermético asegurado mediante su tapa tipo {self.tapa}."

    def transporte(self):
        return f"Transportando la botella de forma cómoda con su forma {self.forma}."

    def manejo(self):
        return f"Manejo ergonómico y seguro debido al diseño {self.diseno}."

    def compatibilidad_bebidas(self):
        return f"Compatible con bebidas calientes y frías según su material {self.material}."

    def reutilizacion(self):
        return "La botella es apta para la reutilización continua."

    def transparencia(self):
        return f"Nivel de visibilidad evaluado por sus grabados '{self.grabados}' y material {self.material}."