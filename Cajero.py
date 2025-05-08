print("Bienvenido Usuario")

DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

students = {
    "2001": {"Nombre": "Camilo Alvarez", "Edad": 22, "Nota": 4.2},
    "2002": {"Nombre": "Paulina Garcia", "Edad": 21, "Nota": 5.0},
    "2003": {"Nombre": "Kevin Castañeda", "Edad": 22, "Nota": 3.0},
    "2004": {"Nombre": "Alejandra Castaño", "Edad": 22, "Nota": 1.0},
    "2005": {"Nombre": "Jose Sanchez", "Edad": 22, "Nota": 3.0}
}

def add_student(student_id, name, age, grade):
    student_id = student_id.strip()
    if student_id in students:
        print(DANGER + "Error: El ID ya se encuentra registrado." + RESET)
        return
    if not (0.0 <= grade <= 5.0):
        print(DANGER + "Error: La nota debe ser de 0.0 a 5.0." + RESET)
        return
    if age <= 0 or not isinstance(age, int):
        print(DANGER + "Error: La edad debe ser un número entero positivo." + RESET)
        return
    students[student_id] = {"Nombre": name.title(), "Edad": age, "Nota": grade}
    print(SUCCESS + "Estudiante añadido correctamente." + RESET)

def search_by_id(student_id):
    student_id = student_id.strip()
    if student_id in students:
        print(SUCCESS + "Estudiante encontrado: " + str(students[student_id]) + RESET)
    else:
        print(WARNING + "ID no encontrado." + RESET)

def search_by_name(name):
    found = False
    for student in students.values():
        if name.lower() in student["Nombre"].lower():
            print(SUCCESS + str(student) + RESET)
            found = True
    if not found:
        print(WARNING + "Estudiante no encontrado." + RESET)

def update_student(student_id, new_age=None, new_grade=None):
    student_id = student_id.strip()
    if student_id not in students:
        print(DANGER + "Error: Estudiante no existe." + RESET)
        return
    if new_age is not None:
        if new_age <= 0 or not isinstance(new_age, int):
            print(DANGER + "Error: La edad debe ser un número entero positivo." + RESET)
            return
        students[student_id]["Edad"] = new_age
    if new_grade is not None:
        if not (0.0 <= new_grade <= 5.0):
            print(DANGER + "Error: La nota debe estar entre 0.0 y 5.0." + RESET)
            return
        students[student_id]["Nota"] = new_grade
    print(SUCCESS + "Información del estudiante actualizada correctamente." + RESET)

def delete_student(student_id):
    student_id = student_id.strip()
    if student_id in students:
        del students[student_id]
        print(SUCCESS + "Estudiante eliminado correctamente." + RESET)
    else:
        print(DANGER + "Error: Estudiante no encontrado." + RESET)

def calculate_average_grade():
    if not students:
        print(WARNING + "No hay estudiantes registrados." + RESET)
        return
    total = sum(student["Nota"] for student in students.values())
    average = total / len(students)
    print(SUCCESS + f"Promedio de nota: {average:.2f}" + RESET)

def list_students_below(threshold=3.0):
    found = False
    for student_id, student in students.items():
        if student["Nota"] < threshold:
            print(f"{DANGER}ID: {student_id}, Nombre: {student['Nombre']}, Nota: {student['Nota']}{RESET}")
            found = True
    if not found:
        print(SUCCESS + f"No hay estudiantes con nota menor a {threshold}" + RESET)

# Menú interactivo
while True:
    print("\n--- Menú de Opciones ---")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante por ID")
    print("3. Buscar estudiante por nombre")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Calcular promedio de notas")
    print("7. Listar estudiantes con nota menor a 3.0")
    print("8. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        sid = input("ID del estudiante: ").strip()
        nombre = input("Nombre: ").strip()
        try:
            edad = int(input("Edad: "))
            nota = float(input("Nota: "))
            add_student(sid, nombre, edad, nota)
        except ValueError:
            print(DANGER + "Edad o nota inválida." + RESET)

    elif opcion == "2":
        sid = input("Ingrese el ID del estudiante: ")
        search_by_id(sid)

    elif opcion == "3":
        nombre = input("Ingrese el nombre (o parte del nombre) del estudiante: ")
        search_by_name(nombre)

    elif opcion == "4":
        sid = input("ID del estudiante a actualizar: ")
        edad_input = input("Nueva edad (deje en blanco si no desea cambiar): ")
        nota_input = input("Nueva nota (deje en blanco si no desea cambiar): ")
        try:
            new_age = int(edad_input) if edad_input else None
            new_grade = float(nota_input) if nota_input else None
            update_student(sid, new_age, new_grade)
        except ValueError:
            print(DANGER + "Edad o nota inválida." + RESET)

    elif opcion == "5":
        sid = input("ID del estudiante a eliminar: ")
        delete_student(sid)

    elif opcion == "6":
        calculate_average_grade()

    elif opcion == "7":
        list_students_below()

    elif opcion == "8":
        print("Saliendo del programa. ¡Hasta pronto!")
        break

    else:
        print(WARNING + "Opción no válida, por favor intente nuevamente." + RESET)
