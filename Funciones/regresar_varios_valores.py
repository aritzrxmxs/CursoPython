print('*** Devolver varios valores de una tupla desde funcion ***')

def persona_mayusculas(nombre, apellido, edad):
    print('Devuelve la tupla en mayusculas')
    return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad = persona_mayusculas('aritz', 'ramos', 29)

print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')