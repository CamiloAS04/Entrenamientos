#Create Inventory and Colors
inventory = {} 
DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

#Funtion for add product
def add_product (inventory,name,price,amount):
    name  = name.lower()
    if name in inventory:
        print(WARNING + "El producto ya existe." + RESET)
        option= input("¿Deseas actualizar la cantidad? (s/n): ").strip().lower()
        while option not in ('s', 'n'):
            option= input("Por favor, responde con 's' o 'n': ").strip().lower()
        if option== 's':
            actually_price, actuallly_amount = inventory[name]
            inventory[name] = (price, actuallly_amount + amount)
            print(SUCCESS + f"Cantidad del producto '{name}' actualizada a {actuallly_amount + amount}." + RESET)
        else:
            print(SUCCESS + "No se realizaron cambios." + RESET)
    else:
        inventory[name] = (price, amount)
        print(SUCCESS + f"Producto '{name}' agregado exitosamente." + RESET)

#Funtion for search product
def search_product(inventory, name):
    name = name.lower()
    product = inventory.get(name)
    if product:
        print(SUCCESS+ f"Producto: {name} | Precio: ${product[0]} | Cantidad: {product[1]}" + RESET)
    else:
        print(WARNING + "Producto no encontrado en el inventario." + RESET)

#Funtion for actualization the price of the product
def actualization_price(inventory, name, new_price):
    name = name.lower()
    if name in inventory:
        _, amount = inventory[name]
        inventory[name] = (new_price,amount)
        print(SUCCESS + f"Precio del producto '{name}' actualizado a ${new_price}." + RESET)
    else:
        print(WARNING + "Producto no encontrado." + RESET)

#Funtion for calculate the total value of inventory
def calculate_total_value (inventory):
    total = sum(map(lambda item: item[0] * item[1], inventory.values()))
    print(SUCCESS + f"Valor total del inventario: ${total:.2f}" + RESET)

#Funtion for eliminated a product
def eliminate_producto(inventory, name):
    name = name.lower()
    if name in inventory:
        del inventory[name]
        print(SUCCESS + f"Producto '{name}' eliminado del inventario." + RESET)
    else:
        print(WARNING+ "Producto no encontrado." + RESET)

#Funtion for show all products
def show_all (inventory):
    if not inventory:
        print(WARNING + "El inventario está vacío." + RESET) 
    else:
        print(SUCCESS + "\n--- LISTA DE PRODUCTOS ---" + RESET)
        for name, (price, amount) in inventory.items():
            print(SUCCESS + f"- {name.capitalize()}: Precio = ${price}, Cantidad = {amount}" + RESET)

#Funtion for validation number
def solicite_number(menssage, is_entero=False):
    while True:
        entrance = input(menssage)
        try:
            value = float(entrance)
            if value < 0:
                print(DANGER + "El número no puede ser negativo." + RESET)
                continue
            return int(value) if is_entero else value
        except ValueError:
            print(DANGER + "Por favor, ingresa un número válido." + RESET)

#Interactive Menu
def menu():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Ver todos los productos")
        print("7. Salir")
        
        option = input("Selecciona una opción (1-7): ").strip()

        if option == "1":
            name = input("Nombre del producto: ").strip()
            while not name:
                name = input("Nombre del producto (no puede estar vacío): ").strip()
            price = solicite_number("Precio del producto: ")
            amount = solicite_number("Cantidad disponible: ", is_entero=True)
            add_product(inventory, name, price, amount)

        elif option == "2":
            name = input("Nombre del producto a consultar: ").strip()
            search_product(inventory, name)
        
        elif option == "3":
            name = input("Nombre del producto a actualizar: ").strip()
            new_price = solicite_number("Nuevo precio: ")
            actualization_price(inventory, name, new_price)
        
        elif option == "4":
            name = input("Nombre del producto a eliminar: ").strip()
            eliminate_producto(inventory, name)
        
        elif option == "5":
            calculate_total_value(inventory)
        
        elif option == "6":
            show_all(inventory)
        
        elif option == "7":
            print("¡Hasta luego!")
            break

        else:
            print(DANGER + "Opción no válida. Intenta de nuevo." + RESET)

# Exacute the program
menu()
        