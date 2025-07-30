# Polimosfirmo

class Animal:
    def hacer_sonido(self):
        print('Hacer pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

# Funcion polimorfica
def hacer_sonido_animal(animal): # Concepto de Duck Typing
    animal.hacer_sonido()

print('*** Ejemplo polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
hacer_sonido_animal(animal1)
print('\nClase Hija Perro: ')
perro1 = Perro()
hacer_sonido_animal(perro1)
print('\nClase hija Gato: ')
gato1 = Gato()
hacer_sonido_animal(gato1)