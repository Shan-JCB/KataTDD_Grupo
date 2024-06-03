class Conjunto:
    def __init__(self, datos, pesos):
        self.__datos = datos
        self.__pesos = pesos

    def promedio_ponderado(self):
        if not self.__datos or not self.__pesos or len(self.__datos) != len(self.__pesos):
            return None

        suma_ponderada = sum(d * p for d, p in zip(self.__datos, self.__pesos))
        suma_pesos = sum(self.__pesos)
        return suma_ponderada / suma_pesos
