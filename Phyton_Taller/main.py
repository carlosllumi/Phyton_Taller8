from inventory import add_product, edit_product, delete_product, list_products, search_product, load_inventory

def main():
    load_inventory()
    option = 0
    while option != 6:
        print("\nSistema de Inventarios")
        print("1. Ingresar producto")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. Buscar producto")
        print("6. Salir")
        option = int(input("Seleccione una opción: "))

        if option == 1:
            add_product()
        elif option == 2:
            edit_product()
        elif option == 3:
            delete_product()
        elif option == 4:
            list_products()
        elif option == 5:
            search_product()
        elif option == 6:
            print("Saliendo del sistema de inventarios.")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
