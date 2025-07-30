class Monitor:

    contador_monitores = 0

    # Constructor

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f'Id Monitor: {self.id_monitor}, Marca: {self.marca}, '
                f'Tamaño: {self.tamanio}"')
if __name__ == '__main__':
    monitor1 = Monitor('AOC', '27')
    print(monitor1)