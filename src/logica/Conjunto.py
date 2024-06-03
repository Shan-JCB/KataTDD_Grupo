class Conjunto:
    def __init__(self, datos, pesos):
        self.__datos = datos
        self.__pesos = pesos

    def promedio_ponderado(self):
        if not self.__datos or not self.__pesos or len(self.__datos) != len(self.__pesos):
            return None
        return sum(d * p for d, p in zip(self.__datos, self.__pesos)) / sum(self.__pesos)

