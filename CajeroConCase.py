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

def entrada_num(msg, tipo=float):
    try:
        return tipo(input(msg))
    except ValueError:
        return None

def mostrar_estudiante(est):
    print(f"Nombre: {est['Nombre']}, Edad: {est['Edad']}, Nota: {est['Nota']}")

while True:
    print("\n--- Menú ---\n1.Agregar 2.Buscar ID 3.Buscar Nombre 4.Actualizar 5.Eliminar 6.Promedio 7.Bajo 3.0 8.Salir")
    opcion = input("Opción: ").strip()

    match opcion:
        case "1":
            sid = input("ID: ").strip()
            if sid in students:
                print(DANGER + "ID ya existe" + RESET)
                continue
            nombre = input("Nombre: ").title()
            edad = entrada_num("Edad: ", int)
            nota = entrada_num("Nota: ")
            if not (edad and 0 <= nota <= 5):
                print(DANGER + "Datos inválidos" + RESET)
                continue
            students[sid] = {"Nombre": nombre, "Edad": edad, "Nota": nota}
            print(SUCCESS + "Agregado" + RESET)

        case "2":
            sid = input("ID: ").strip()
            est = students.get(sid)
            print(SUCCESS + str(est) + RESET if est else WARNING + "No encontrado" + RESET)

        case "3":
            nombre = input("Nombre: ").lower()
            encontrados = [est for est in students.values() if nombre in est["Nombre"].lower()]
            if encontrados:
                for est in encontrados:
                    mostrar_estudiante(est)
            else:
                print(WARNING + "No hay coincidencias" + RESET)

        case "4":
            sid = input("ID: ").strip()
            if sid not in students:
                print(DANGER + "No existe" + RESET)
                continue
            edad = input("Nueva edad (enter para ignorar): ")
            nota = input("Nueva nota (enter para ignorar): ")
            if edad.isdigit():
                students[sid]["Edad"] = int(edad)
            if nota.replace(".", "", 1).isdigit():
                val = float(nota)
                if 0 <= val <= 5:
                    students[sid]["Nota"] = val
            print(SUCCESS + "Actualizado" + RESET)

        case "5":
            sid = input("ID: ").strip()
            if sid in students:
                del students[sid]
                print(SUCCESS + "Eliminado" + RESET)
            else:
                print(DANGER + "No existe" + RESET)

        case "6":
            if not students:
                print(WARNING + "Sin registros" + RESET)
                continue
            promedio = sum(s["Nota"] for s in students.values()) / len(students)
            print(SUCCESS + f"Promedio general: {promedio:.2f}" + RESET)

        case "7":
            bajos = [f"{id}: {s['Nombre']} ({s['Nota']})" for id, s in students.items() if s["Nota"] < 3.0]
            print("\n".join(bajos) if bajos else SUCCESS + "Todos con nota >= 3.0" + RESET)

        case "8":
            print("Hasta luego")
            break

        case _:
            print(WARNING + "Opción inválida" + RESET)
