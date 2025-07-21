print('*** Alcance de variables ***')

contador_global = 0

def incrementar_contador():
    # declaramos una variable local
    contador_local = 0

    # Usar la variable global

    global contador_global
    contador_global += 1

    # Incrementar la variabler local
    contador_local += 1

    # Imprimir ambos contadores

    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias veecs a la funcion

incrementar_contador()
incrementar_contador()
incrementar_contador()


print(f'Valor de variable global: {contador_global}')