import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):

    def test_conjunto_vacio_retornaNone(self):
        datos = []
        pesos = []
        conjunto = Conjunto(datos, pesos)
        resultado = conjunto.promedio_ponderado()
        self.assertIsNone(resultado)

class TestConjunto(unittest.TestCase):
    def test_promedio_ponderado_0(self):
        datos = [10, 12, 14]
        pesos = [3, 4, 2]
        conjunto = Conjunto(datos, pesos)
        resultado = conjunto.promedio_ponderado()
        self.assertAlmostEqual(resultado, 11.78, places=2)

    def test_promedio_ponderado_1(self):
        datos = [15, 15, 17]
        pesos = [3, 4, 2]
        conjunto = Conjunto(datos, pesos)
        resultado = conjunto.promedio_ponderado()
        self.assertAlmostEqual(resultado, 15.44, places=2)




if __name__ == '__main__':
    unittest.main()
