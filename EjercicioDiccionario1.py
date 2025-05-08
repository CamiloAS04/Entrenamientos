# Diccionario vacío para comenzar
biblioteca = {}

# Agregar un nuevo libro
id_nuevo = input("Ingrese ID del nuevo libro: ")
if id_nuevo not in biblioteca:
    titulo = input("Ingrese título: ")
    autor = input("Ingrese autor: ")
    año = int(input("Ingrese año de publicación: "))
    biblioteca[id_nuevo] = {'titulo': titulo, 'autor': autor, 'año': año}
    print("Libro agregado.")
else:
    print("Ese ID ya existe.")

# Mostrar todos los libros
print("\nLibros en la biblioteca:")
for id_libro, datos in biblioteca.items():
    print(f"{id_libro}: {datos}")

# Buscar libro por ID o Título
busqueda = input("\nBuscar libro por ID o Título: ").lower()
encontrado = False
for id_libro, datos in biblioteca.items():
    if busqueda == id_libro or busqueda == datos['titulo'].lower():
        print(f"Libro encontrado: {id_libro}: {datos}")
        encontrado = True
        break
if not encontrado:
    print("Libro no encontrado.")

# Actualizar libro
id_actualizar = input("\nID del libro a actualizar: ")
if id_actualizar in biblioteca:
    nuevo_autor = input("Nuevo autor: ")
    nuevo_año = int(input("Nuevo año: "))
    biblioteca[id_actualizar]['autor'] = nuevo_autor
    biblioteca[id_actualizar]['año'] = nuevo_año
    print("Libro actualizado.")
else:
    print("ID no encontrado.")

# Eliminar libro
id_eliminar = input("\nID del libro a eliminar: ")
if id_eliminar in biblioteca:
    del biblioteca[id_eliminar]
    print("Libro eliminado.")
else:
    print("ID no encontrado.")

# Mostrar estado final
print("\nEstado final de la biblioteca:")
for id_libro, datos in biblioteca.items():
    print(f"{id_libro}: {datos}")