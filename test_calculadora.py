import unittest
from unittest import TestCase
from calculadora import Calculadora


class TestCalculadora(TestCase):
    def test_sumar_dos_mas_dos(self):
        calc = Calculadora()
        resultado = calc.sumar(2, 2)
        self.assertEqual(4, resultado)

    def test_ingresa_caracter(self):
        calc = Calculadora()
        resultado = calc.sumar('X', 2)
        self.assertEqual('Sólo se admiten números', resultado)


if __name__ == '__main__':
    unittest.main()
