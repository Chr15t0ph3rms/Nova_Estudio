#import flet as ft

from dao.inventario_dao import InventarioDAO

from modelos.inventario import Inventario


def ver_inventario():
    try:
        inventario_dao = InventarioDAO()
        inventarios = inventario_dao.obtener_todo()

        if len(inventarios) == 0:
            print("No hay inventarios registrado")
        else:
            for inventario in inventarios:
                print(f" {inventario.id_inventario} - {inventario.nombre} - { inventario.tipo} - {inventario.estado} - {inventario.cantidad} - {inventario.disponible}" )
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
        print("Error")
        print(e)

def insertar_inventario():
    print("INSERTAR UN NUEVO INVENTARIO")
    nombre = input("Escribe el nombre: ")
    tipo = input("Escribe el tipo: ")
    estado = input("Escribe el estado: ")
    cantidad = int(input("Escribe la cantidad: "))
    disponible = True
  
    try:
        inventario_dao = InventarioDAO()
        ultimo_id = inventario_dao.obtener_ultimo_id() + 1
        inventario = Inventario(ultimo_id, nombre, tipo, estado, cantidad, disponible)
        inventario_dao.insertar(inventario)
        print("Inserción del nuevo inventario fue exitosa")
    except Exception as e:
        print("Error al insertar el inventario")
        print(e)


def actualizar_inventario():
    try:
        inventario_dao = InventarioDAO()
        print("Lista de inventarios disponibles")
        ver_inventario()
        id = int(input("Seleccione el id del inventario a actualizar"))
        nombre = input("Escribe el nombre: ")
        tipo = input("Escribe el tipo: ")
        estado = input("Escribe el estado: ")
        cantidad = int(input("Escribe la cantidad: "))
        disponible = bool(input("Escribe si está disponible: "))
        inventario = Inventario(id, nombre, tipo, estado, cantidad, disponible)
        inventario_dao.actualizar(inventario)
        print("El inventario fue actualizado con éxito")
    except Exception as e:
        print("Error al actualizar el inventario")
        print(e)

def eliminar_inventario():
    try:
        inventario_dao = InventarioDAO()
        print("Lista de inventarios disponibles")
        ver_inventario()
        id = int(input("Escriba el id del inventario a eliminar: "))
        inventario_dao.eliminar(id)
        print(f"El inventario {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el inventario {id}")
        print(e)


def menu_inventario():
    print("1. Ver todos los inventarios")
    print("2. Insertar un nuevo inventario")
    print("3. Actualizar un inventario existente")
    print("4. Eliminar un inventario existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1: 
            ver_inventario()
        case 2: 
            insertar_inventario()
        case 3:
            actualizar_inventario()
        case 4: 
            eliminar_inventario()   
#ft.app(target=main_window)

def main():
    print("=== BIBLIOTECA UNIVERSITARIA === ")
    print("Menú de opciones:")
    print("1. Inventario")
    opcion = int(input("Escribe tu opción: "))
    match opcion:
        case 1: menu_inventario()

    print("Saliendo del sistema de Biblioteca universitaria ... ")
   

if __name__ == "__main__":
    main()