from sistema_bibliotecas.biblioteca import Biblioteca
from sistema_bibliotecas.libro import Libro

bibliotecaNacional = Biblioteca('Nacional')
print(f'Bienvenidos a la Biblioteca {bibliotecaNacional.nombre}')
libro1 = Libro('Don Quijote', 'Cervantes', 'Ficcion')
libro2 = Libro('Harry Potter', 'J.K Rowling', 'Magia')
libro3 = Libro('El Señor de Los anillos', 'No se', 'Ficcion')

bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
print(f'Libros de Cervantes: ')
bibliotecaNacional.buscar_libros_por_autor('Cervantes')
print(f'\nLibros de ficción: ')
bibliotecaNacional.buscar_libros_por_genero('Ficcion')
print()
bibliotecaNacional.mostrar_todos_los_libros()

