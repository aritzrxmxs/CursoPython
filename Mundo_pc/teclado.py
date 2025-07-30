from Mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'Id Teclado: {self.id_teclado}, Marca: {self.marca}, '
                f'Tipo entrada: {self.tipo_entrada}')

# Prueba en codigo principal

if __name__ == '__main__':
    teclado1 = Teclado('Logitech', 'Wifi')
    print(teclado1)