class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def suma(self):
        print(f'El resultado de la suma es: {self.operando1 + self.operando2}')

    def resta(self):
        print(f'El resultado de la resta es: {self.operando1 - self.operando2}')
    def multiplicacion(self):
        print(f'El resultado de la multiplicación es: {self.operando1 * self.operando2}')
    def division(self):
        print(f'El resultado de la división es: {self.operando1 / self.operando2}')


if __name__ == '__main__':
    aritmetica = Aritmetica(2, 8)
    aritmetica.suma()
    aritmetica.resta()
    aritmetica.multiplicacion()
    aritmetica.division()