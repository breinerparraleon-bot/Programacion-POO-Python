from botella import Botella

class BotellaVidrio(Botella):
    def __init__(self, capacidad, forma, diseno, tapa, grabados, tipo_vidrio="Transparente"):
        super().__init__("Vidrio", capacidad, forma, diseno, tapa, grabados)
        self.__tipo_vidrio = tipo_vidrio

    def get_tipo_vidrio(self):
        return self.__tipo_vidrio

    def set_tipo_vidrio(self, tipo):
        self.__tipo_vidrio = tipo

    def esterilizar(self):
        return f"Esterilizando la botella de vidrio tipo {self.__tipo_vidrio} a altas temperaturas."