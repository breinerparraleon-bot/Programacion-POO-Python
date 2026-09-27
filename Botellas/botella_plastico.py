from botella import Botella

class BotellaPlastico(Botella):
    def __init__(self, capacidad, forma, diseno, tapa, grabados, es_reciclable=True):
        super().__init__("Plástico", capacidad, forma, diseno, tapa, grabados)
        self.__es_reciclable = es_reciclable

    def get_es_reciclable(self):
        return self.__es_reciclable

    def set_es_reciclable(self, reciclable):
        self.__es_reciclable = reciclable

    def aplastar(self):
        if self.__es_reciclable:
            return "La botella de plástico se ha aplastado para facilitar su reciclaje."
        return "No se puede aplastar."