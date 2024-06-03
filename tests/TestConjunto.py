import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):

    def test_conjunto_vacio_retornaNone(self):
        datos = []
        pesos = []
        conjunto = Conjunto(datos, pesos)
        resultado = conjunto.promedio_ponderado()
        self.assertIsNone(resultado)

    def test_conjunto_un_elemento(self):
        datos = [10]
        pesos = [1]
        conjunto = Conjunto(datos, pesos)
        resultado = conjunto.promedio_ponderado()
        self.assertEqual(resultado, 10)


if __name__ == '__main__':
    unittest.main()
