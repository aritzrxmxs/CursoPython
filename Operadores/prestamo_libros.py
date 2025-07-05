print('*** Préstamo de Libros ***')
DISTANCIA_PERMITIDA = 3
tiene_carnet = input('Tienes carnet de estudiante? (Si/No) ')
distancia = int(input('A cuantos kms vives? '))
cumple_requisitos = (tiene_carnet.strip().lower() == 'si'
                     or distancia <= DISTANCIA_PERMITIDA)
print(f'Tiene derecho al prestamo de libros: {cumple_requisitos}')