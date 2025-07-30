from Mundo_pc.computadora import Computadora
from Mundo_pc.monitor import Monitor
from Mundo_pc.orden import Orden
from Mundo_pc.raton import Raton
from Mundo_pc.teclado import Teclado

print('*** Mundo PC ***')

# Ordenador 1
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('Logitech', 'wifi')
monitor1 = Monitor('AOC', '15')
computadora1 = Computadora('MSI', monitor1, teclado1, raton1)

# Ordenador 2
teclado2 = Teclado('NewSkill', 'USB')
raton2 = Raton('Logitech', 'wifi')
monitor2 = Monitor('Sony', '27')
computadora2 = Computadora('HP', monitor2, teclado2, raton2)


# Crear la lista de computadoras

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

# Ordenador 3
teclado3 = Teclado('Logitech', 'USB')
raton3 = Raton('Razer', 'wifi')
monitor3 = Monitor('Samsung', '24')
computadora3 = Computadora('MSI', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)

