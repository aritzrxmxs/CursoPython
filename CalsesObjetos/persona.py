# Definicion de una clase


class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Direccion de memoria self: {id(persona1)}')
        print(f'Direccion de memoria hexadecimal self: {hex(id(persona1))}')

# Creando objetos

if __name__ == '__main__':
    # Crear el primer objeto
    persona1 = Persona('Aritz', 'Ramos') # Creamos objeto vacío
    persona1.mostrar_persona()
    print(f'Direccion de memoria persona 1: {id(persona1)}')
    print(f'Direccion de memoria hexadecimal persona 1: {hex(id(persona1))}')

    # Creamos un segundo objeto
    persona2 = Persona('Victoria', 'Acosta')
    persona2.mostrar_persona()
    print(f'Direccion de memoria persona 2: {id(persona2)}')
    print(f'Direccion de memoria hexadecimal persona 2: {hex(id(persona2))}')