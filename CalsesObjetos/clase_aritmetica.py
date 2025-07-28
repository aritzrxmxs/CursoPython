class Aritmetica:

    # def __init__(self, operando1):
    #       self.operando1 = operando1

    def __init__(self, operando1=None, operando2=None):
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
    print()
    aritmetica2 = Aritmetica(5, 7)
    aritmetica2.suma()
    aritmetica2.resta()
    aritmetica2.multiplicacion()
    aritmetica2.division()
    print()
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.suma()
    print()
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = int(input('Numero 1: '))
    aritmetica4.operando2 = int(input('Numero 2: '))
    aritmetica4.suma()