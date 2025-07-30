from Mundo_pc.monitor import Monitor
from Mundo_pc.raton import Raton
from Mundo_pc.teclado import Teclado


class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self. nombre = nombre
        self.monitor = monitor
        self. teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Ratón: {self.raton}'''

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('Logitech', 'wifi')
    monitor1 = Monitor('AOC', 'HDMI')
    computadora1 = Computadora('MSI', monitor1, teclado1, raton1)
    print(computadora1)
