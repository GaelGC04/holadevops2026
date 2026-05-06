
class Calculadora:
    def sumar(self, num1, num2):
        try:
            resultado = num1 + num2
        except TypeError:
            resultado = 'Sólo se admiten números'

        return resultado
