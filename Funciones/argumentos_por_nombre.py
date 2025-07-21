print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional

imprimir_persona('Aritz', 'Ramos', 29)

# Llamar a la funcion usando los argumentos por nombre

imprimir_persona(nombre='Aritz', apellido='Ramos', edad=29)

# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden

imprimir_persona(edad=29, apellido='Ramos', nombre='Aritz')

# Argumentos con valores por default

imprimir_persona(nombre='Aritz')