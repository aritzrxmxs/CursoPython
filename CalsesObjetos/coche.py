# Difinimos la clase coche
class Coche:

        def __init__(self, marca, modelo, color):
            self._marca = marca # Atributo publico
            self._modelo = modelo # Atributo protegido
            self._color = color # Atributo privado


        def conducir(self):
            print(f'''Conduciendo el coche:
            Marca: {self._marca}
            Modelo: {self._modelo}
            Color: {self._color}''')

        # def get_marca(self):
        #     return self._marca

        @property # Definir el metodo get de manera mas phytonica
        def marca(self):
            return self._marca

        @marca.setter
        def marca(self, marca):
            self._marca = marca

        @property
        def modelo(self):
            return self._modelo
        @modelo.setter
        def modelo(self, modelo):
            self._modelo = modelo

        @property
        def color(self):
            return self._color
        @color.setter
        def color(self, color):
            self._color = color
# Programa principal (Main)

if __name__ == '__main__':
    # Creamos un coche
    coche1 = Coche('Kia', 'Ceed', 'Blanco')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Kia 2'
    coche1.modelo = 'Ceed 2' # Esto no es una buena practica
    coche1.color = 'Blanco 2' # Ignora la modificacion porque es privado
    # Intentar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'Valor nuevo atributo')
    coche1.conducir()
    print(coche1.nuevo_atributo)
    # Atributo marca coche 1
    coche1.marca = 'Kia 3'
    print(f'Atributo marca coche1: {coche1.marca}')
    # Segundo objeto
    coche2 = Coche('Toyota', 'Yaris', 'Negro')
    coche2.conducir()

