import datetime

# Base de datos simulada
reservas = []
contador_id = 1

# Tarifas
PRECIOS_BASE = {
    "nacional": 230000,
    "internacional": 4200000
}

COSTOS_EQUIPAJE = [
    (20, 50000),
    (30, 70000),
    (50, 110000)
]

def generar_id():
    global contador_id
    id_generado = f"COMP{contador_id:04d}"
    contador_id += 1
    return id_generado

def obtener_costo_equipaje(peso):
    if peso > 50:
        return None  # No admitido
    for limite, costo in COSTOS_EQUIPAJE:
        if peso <= limite:
            return costo
    return 0

def registrar_reserva():
    print("\n--- Registro de Reserva ---")
    nombre = input("Nombre del pasajero: ")
    tipo_viaje = input("Tipo de viaje (nacional/internacional): ").lower()
    destino = "Bogotá → Medellín" if tipo_viaje == "nacional" else "Bogotá → España"
    fecha = input("Fecha del viaje (YYYY-MM-DD): ")

    try:
        fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        print("⚠️ Fecha inválida.")
        return

    try:
        peso_principal = float(input("Peso del equipaje principal (kg): "))
    except ValueError:
        print("⚠️ Peso inválido.")
        return

    estado_equipaje_principal = "Admitido"
    costo_equipaje = obtener_costo_equipaje(peso_principal)
    if costo_equipaje is None:
        estado_equipaje_principal = "No admitido"
        costo_equipaje = 0

    equipaje_mano = input("¿Lleva equipaje de mano? (sí/no): ").lower()
    estado_mano = "No lleva"
    if equipaje_mano == "sí":
        try:
            peso_mano = float(input("Peso del equipaje de mano (kg): "))
            if peso_mano > 13:
                estado_mano = "Rechazado"
            else:
                estado_mano = "Admitido"
        except ValueError:
            print("⚠️ Peso inválido.")
            return

    id_compra = generar_id()
    precio_base = PRECIOS_BASE[tipo_viaje]
    total = precio_base + costo_equipaje

    reserva = {
        "id": id_compra,
        "nombre": nombre,
        "tipo": tipo_viaje,
        "destino": destino,
        "fecha": fecha,
        "equipaje_principal": estado_equipaje_principal,
        "equipaje_mano": estado_mano,
        "costo_total": total
    }
    reservas.append(reserva)

    # Resumen individual
    print("\n✅ Reserva registrada exitosamente:")
    print(f"ID de compra: {id_compra}")
    print(f"Nombre: {nombre}")
    print(f"Destino: {destino}")
    print(f"Fecha: {fecha}")
    print(f"Estado equipaje principal: {estado_equipaje_principal}")
    print(f"Estado equipaje de mano: {estado_mano}")
    print(f"Costo total del viaje: ${total:,.0f}")

def consultar_compra():
    id_busqueda = input("Ingrese el ID de compra a consultar: ").strip().upper()
    encontrado = False
    for r in reservas:
        if r["id"] == id_busqueda:
            encontrado = True
            print(f"\n🧾 Detalles de la compra {r['id']}")
            for clave, valor in r.items():
                if clave != 'id':
                    print(f"{clave.capitalize()}: {valor}")
    if not encontrado:
        print("❌ No se encontró una reserva con ese ID.")

def reporte_final():
    print("\n--- Reporte Final del Sistema ---")
    total_recaudado = sum(r["costo_total"] for r in reservas)
    total_pasajeros = len(reservas)
    total_nacionales = sum(1 for r in reservas if r["tipo"] == "nacional")
    total_internacionales = total_pasajeros - total_nacionales

    print(f"Total recaudado: ${total_recaudado:,.0f}")
    print(f"Número total de pasajeros: {total_pasajeros}")
    print(f"Nacionales: {total_nacionales}")
    print(f"Internacionales: {total_internacionales}")

    fecha_especifica = input("¿Desea consultar el total por una fecha específica? (YYYY-MM-DD, enter para omitir): ")
    if fecha_especifica:
        try:
            fecha_obj = datetime.datetime.strptime(fecha_especifica, "%Y-%m-%d").date()
            total_por_fecha = sum(r["costo_total"] for r in reservas if r["fecha"] == fecha_obj)
            print(f"Total recaudado el {fecha_especifica}: ${total_por_fecha:,.0f}")
        except ValueError:
            print("⚠️ Fecha inválida.")

def menu():
    while True:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. Registrar reserva")
        print("2. Consultar reserva por ID")
        print("3. Ver reporte final (admin)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            consultar_compra()
        elif opcion == "3":
            reporte_final()
        elif opcion == "4":
            print("👋 Gracias por usar el sistema.")
            break
        else:
            print("❌ Opción no válida.")

# Ejecutar menú principal
menu()
