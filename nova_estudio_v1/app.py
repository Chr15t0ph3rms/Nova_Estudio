#import flet as ft

from dao.inventario_dao import InventarioDAO
from dao.empleados_dao import EmpleadosDAO
from dao.eventos_dao import EventosDAO
from dao.paquetes_dao import PaquetesDAO

from modelos.inventario import Inventario
from modelos.empleados import Empleados
from modelos.eventos import Eventos
from modelos.paquetes import Paquetes

#Inventario
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

#empleados-------------------------------------------------------------------------
def ver_empleados():
    try:
        empleados_dao = EmpleadosDAO()
        empleados = empleados_dao.obtener_todo()

        if len(empleados) == 0:
            print("No hay empleados registrado")
        else:
            for empleado in empleados:
                print(f" {empleado.id_empleados} - {empleado.nombre} - {empleado.app} - {empleado.apm} - {empleado.puesto} - {empleado.telefono}")
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
        print("Error")
        print(e)

def insertar_empleado():
    print("INSERTAR UN NUEVO EMPLEADO")
    id_empleado = input("Escribe el ID del empleado: ")
    nombre = input("Escribe el nombre: ")
    app = input("Escribe el apellido paterno: ")
    apm = input("Escribe el apellido materno: ")
    puesto = input("Escribe el puesto: ")
    telefono = input("Escribe el teléfono: ")

    try:
        empleados_dao = EmpleadosDAO()
        ultimo_id = empleados_dao.obtener_ultimo_id() + 1
        empleado = Empleados(id_empleado, nombre, app, apm, puesto, telefono)
        empleados_dao.insertar(empleado)
        print("Inserción del nuevo empleado fue exitosa")
    except Exception as e:
        print("Error al insertar el empleado")
        print(e)

def actualizar_empleado():
    try:
        empleados_dao = EmpleadosDAO()
        print("Lista de empleados disponibles")
        ver_empleados()
        id = int(input("Seleccione el id del empleado a actualizar: "))
        nombre = input("Escribe el nombre: ")
        app = input("Escribe el apellido paterno: ")
        apm = input("Escribe el apellido materno: ")
        puesto = input("Escribe el puesto: ")
        telefono = input("Escribe el teléfono: ")
        empleado = Empleados(id, nombre, app, apm, puesto, telefono)
        empleados_dao.actualizar(empleado)
        print("El empleado fue actualizado con éxito")
    except Exception as e:
        print("Error al actualizar el empleado")
        print(e)

def eliminar_empleado():
    try:
        empleados_dao = EmpleadosDAO()
        print("Lista de empleados disponibles")
        ver_empleados()
        id = int(input("Escriba el id del empleado a eliminar: "))
        empleados_dao.eliminar(id)
        print(f"El empleado {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el empleado {id}")
        print(e)

#eventos-------------------------------------------------------------------------
def ver_eventos():
    try:
        eventos_dao = EventosDAO()
        eventos = eventos_dao.obtener_todo()

        if len(eventos) == 0:
            print("No hay eventos registrados")
        else:
            for evento in eventos:
                print(f" {evento.id_evento} - {evento.nombre} - {evento.fecha} - {evento.hora} - {evento.calle} - {evento.colonia} - {evento.numero_exterior} - {evento.costo}")
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
        print("Error")
        print(e)

def insertar_evento():
    print("INSERTAR UN NUEVO EVENTO")
    id_evento = input("Escribe el ID del evento: ")
    nombre = input("Escribe el nombre: ")
    fecha = input("Escribe la fecha: ")
    hora = input("Escribe la hora: ")
    calle = input("Escribe la calle: ")
    colonia = input("Escribe la colonia: ")
    numero_exterior = input("Escribe el número exterior: ")
    costo = input("Escribe el costo: ")


    try:
        eventos_dao = EventosDAO()
        ultimo_id = eventos_dao.obtener_ultimo_id() + 1
        evento = Eventos(id_evento, nombre, fecha, hora, calle, colonia, numero_exterior, costo)
        eventos_dao.insertar(evento)
        print("Inserción del nuevo evento fue exitosa")
    except Exception as e:
        print("Error al insertar el evento")
        print(e)

def actualizar_evento():
    try:
        eventos_dao = EventosDAO()
        print("Lista de eventos disponibles")
        ver_eventos()
        id = int(input("Seleccione el id del evento a actualizar: "))
        nombre = input("Escribe el nombre: ")
        fecha = input("Escribe la fecha: ")
        hora = input("Escribe la hora: ")
        calle = input("Escribe la calle: ")
        colonia = input("Escribe la colonia: ")
        numero_exterior = input("Escribe el número exterior: ")
        costo = input("Escribe el costo: ")
        evento = Eventos(id, nombre, fecha, hora, calle, colonia, numero_exterior, costo)
        eventos_dao.actualizar(evento)
        print("El evento fue actualizado con éxito")
    except Exception as e:
        print("Error al actualizar el evento")
        print(e)

def eliminar_evento():
    try:
        eventos_dao = EventosDAO()
        print("Lista de eventos disponibles")
        ver_eventos()
        id = int(input("Escriba el id del evento a eliminar: "))
        eventos_dao.eliminar(id)
        print(f"El evento {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el evento {id}")
        print(e)

#paquetes-------------------------------------------------------------------------
def ver_paquetes():
    try:
        paquetes_dao = PaquetesDAO()
        paquetes = paquetes_dao.obtener_todo()

        if len(paquetes) == 0:
            print("No hay paquetes registrados")
        else:
            for paquete in paquetes:
                print(f" {paquete.id_paquetes} - {paquete.nombre} - {paquete.tipo_paquete} - {paquete.costo} - {paquete.descripcion}")
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
        print("Error")
        print(e)

def insertar_paquetes():
    print("INSERTAR UN NUEVO PAQUETE")
    id_paquete = input("Escribe el ID del paquete: ")
    nombre = input("Escribe el nombre: ")
    tipo_paquete = input("Escribe el tipo de paquete: ")
    costo = input("Escribe el costo: ")
    descripcion = input("Escribe la descripción: ")

    try:
        paquetes_dao = PaquetesDAO()
        ultimo_id = paquetes_dao.obtener_ultimo_id() + 1
        paquete = Paquetes(id_paquete, nombre, tipo_paquete, costo, descripcion)
        paquetes_dao.insertar(paquete)
        print("Inserción del nuevo paquete fue exitosa")
    except Exception as e:
        print("Error al insertar el paquete")
        print(e)

def actualizar_paquetes():
    try:
        paquetes_dao = PaquetesDAO()
        print("Lista de paquetes disponibles")
        ver_paquetes()
        id = int(input("Seleccione el id del paquete a actualizar: "))
        nombre = input("Escribe el nombre: ")
        tipo_paquete = input("Escribe el tipo de paquete: ")
        costo = input("Escribe el costo: ")
        descripcion = input("Escribe la descripción: ")
        paquete = Paquetes(id, nombre, tipo_paquete, costo, descripcion)
        paquetes_dao.actualizar(paquete)
        print("El paquete fue actualizado con éxito")
    except Exception as e:
        print("Error al actualizar el paquete")
        print(e)

def eliminar_paquetes():
    try:
        paquetes_dao = PaquetesDAO()
        print("Lista de paquetes disponibles")
        ver_paquetes()
        id = int(input("Escriba el id del paquete a eliminar: "))
        paquetes_dao.eliminar(id)
        print(f"El paquete {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el paquete {id}")
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

def menu_empleados():
    print("1. Ver todos los empleados")
    print("2. Insertar un nuevo empleado")
    print("3. Actualizar un empleado existente")
    print("4. Eliminar un empleado existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_empleados()
        case 2:
            insertar_empleado()
        case 3:
            actualizar_empleado()
        case 4:
            eliminar_empleado()

def menu_eventos():
    print("1. Ver todos los eventos")
    print("2. Insertar un nuevo evento")
    print("3. Actualizar un evento existente")
    print("4. Eliminar un evento existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_eventos()
        case 2:
            insertar_evento()
        case 3:
            actualizar_evento()
        case 4:
            eliminar_evento()

def menu_paquetes():
    print("1. Ver todos los paquetes")
    print("2. Insertar un nuevo paquete")
    print("3. Actualizar un paquete existente")
    print("4. Eliminar un paquete existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_paquetes()
        case 2:
            insertar_paquetes()
        case 3:
            actualizar_paquetes()
        case 4:
            eliminar_paquetes()
#ft.app(target=main_window)

def main():
    while True:
        print("=== Nova Estudio === ")
        print("Menú de opciones:")
        print("1. Inventario")
        print("2. Empleados")
        print("3. Eventos")
        print("4. Paquetes")
        print("5. Salir")
        opcion = int(input("Escribe tu opción: "))

        if opcion == 1:
            menu_inventario()
        elif opcion == 2:
            menu_empleados()
        elif opcion == 3:
            menu_eventos()
        elif opcion == 4:
            menu_paquetes()
        elif opcion == 5:
            print("Saliendo del sistema de Nova Estudio ... ")
            break
        else:
            print("Opción no válida")
   

if __name__ == "__main__":
    main()