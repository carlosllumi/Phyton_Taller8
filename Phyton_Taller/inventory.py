import pickle

MAX_PRODUCTS = 100

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

inventory = []
product_count = 0

def load_inventory():
    global inventory, product_count
    try:
        with open('inventory.pkl', 'rb') as f:
            inventory = pickle.load(f)
            product_count = len(inventory)
    except FileNotFoundError:
        inventory = []
        product_count = 0

def save_inventory():
    with open('inventory.pkl', 'wb') as f:
        pickle.dump(inventory, f)

def add_product():
    global product_count
    if product_count >= MAX_PRODUCTS:
        print("Inventario lleno, no se pueden agregar más productos.")
        return
    name = input("Ingrese el nombre del producto: ")
    quantity = int(input("Ingrese la cantidad del producto: "))
    price = float(input("Ingrese el precio del producto: "))
    inventory.append(Product(name, quantity, price))
    product_count += 1
    print("Producto agregado con éxito.")
    save_inventory()

def edit_product():
    name = input("Ingrese el nombre del producto a editar: ")
    for product in inventory:
        if product.name == name:
            print("Producto encontrado. Ingrese los nuevos datos.")
            product.name = input("Ingrese el nuevo nombre del producto: ")
            product.quantity = int(input("Ingrese la nueva cantidad del producto: "))
            product.price = float(input("Ingrese el nuevo precio del producto: "))
            print("Producto editado con éxito.")
            save_inventory()
            return
    print("Producto no encontrado.")

def delete_product():
    global product_count
    name = input("Ingrese el nombre del producto a eliminar: ")
    for i, product in enumerate(inventory):
        if product.name == name:
            del inventory[i]
            product_count -= 1
            print("Producto eliminado con éxito.")
            save_inventory()
            return
    print("Producto no encontrado.")

def list_products():
    if product_count == 0:
        print("No hay productos en el inventario.")
        return
    print("Listado de productos:")
    for i, product in enumerate(inventory):
        print(f"Producto {i + 1}:")
        print(f"Nombre: {product.name}")
        print(f"Cantidad: {product.quantity}")
        print(f"Precio: {product.price:.2f}")

def search_product():
    name = input("Ingrese el nombre del producto a buscar: ")
    for product in inventory:
        if product.name == name:
            print("Producto encontrado:")
            print(f"Nombre: {product.name}")
            print(f"Cantidad: {product.quantity}")
            print(f"Precio: {product.price:.2f}")
            return
    print("Producto no encontrado.")
