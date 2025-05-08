# Dar la bienvenida al cajero
print("¡Bienvenido usuario!")

# Crear el diccionario e historial
informacion_usuario = {
    "Nombre": "Camilo",
    "Numero de cuenta": ("5968203"),
    "Saldo Actual": 5000000
}

historial = []

# Definir función para consultar el saldo
def consultar_saldo():
    print(f"\nSaldo actual: ${informacion_usuario['Saldo Actual']:,}")

# Definir función para retirar saldo
def retirar_saldo():
    cantidad = int(input("¿Cuánto deseas retirar? $"))
    if cantidad > informacion_usuario["Saldo Actual"]:
        print("Saldo insuficiente")
        historial.append(f"Intento fallido de retiro: ${cantidad:,}")
    else:
        informacion_usuario["Saldo Actual"] -= cantidad
        print(f"Has retirado ${cantidad:,}. Nuevo saldo: ${informacion_usuario['Saldo Actual']:,}")
        historial.append(f"Retiro: ${cantidad:,}")

# Definir función para depositar saldo
def depositar_saldo():
    cantidad = int(input("¿Cuánto deseas depositar? $"))
    informacion_usuario["Saldo Actual"] += cantidad
    print(f"Has depositado ${cantidad:,}. Nuevo saldo: ${informacion_usuario['Saldo Actual']:,}")
    historial.append(f"Depósito: ${cantidad:,}")

# Definir función para mostrar el historial de movimientos
def mostrar_historial():
    print("\n--- Historial de movimientos ---")
    if not historial:
        print("No hay movimientos registrados")
    else:
        for movimiento in historial:
            print("-", movimiento)

# Crear menú interactivo
while True:
    print("\n-- Menú de opciones --")
    print("1. Consultar Saldo")
    print("2. Retirar Saldo")
    print("3. Depositar dinero")
    print("4. Mostrar Historial")
    print("5. Salir")
    
    opcion = input("Ingrese una opción (1-5): ")
    
    if opcion == "1":
        consultar_saldo()
    elif opcion == "2":
        retirar_saldo()
    elif opcion == "3":
        depositar_saldo()
    elif opcion == "4":
        mostrar_historial()
    elif opcion == "5":
        print("¡Gracias por usar el cajero!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
