import unittest
from unittest import TestCase
from calculadora import Calculadora


class TestCalculadora(TestCase):
    def test_sumar_dos_mas_dos(self):
        calc = Calculadora()
        resultado = calc.sumar(3, 2)
        self.assertEqual(4, resultado)


if __name__ == '__main__':
    unittest.main()
