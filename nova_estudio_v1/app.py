#import flet as ft

from dao.inventario_dao import InventarioDAO
from dao.empleados_dao import EmpleadosDAO
from dao.eventos_dao import EventosDAO
from dao.paquetes_dao import PaquetesDAO
from dao.agencia_dao import AgenciaDAO
from dao.cliente_dao import ClienteDAO
from dao.contrato_dao import ContratoDAO

from modelos.inventario import Inventario
from modelos.empleados import Empleados
from modelos.eventos import Eventos
from modelos.paquetes import Paquetes
from modelos.agencia import Agencia
from modelos.cliente import Cliente
from modelos.contrato import Contrato

#Inventario-------------------------------------------------------------------------
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

#Empleados-------------------------------------------------------------------------
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

#Eventos-------------------------------------------------------------------------
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

#Paquetes-------------------------------------------------------------------------
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
        case _:
            print("Opción no válida")

#Agencia-------------------------------------------------------------------------
def ver_agencia():
    try:
        agencias_dao = AgenciaDAO()
        agencias = agencias_dao.obtener_todo()

        if len(agencias) == 0:
            print("No hay agencias registradas")
        else:
            for agencia in agencias:
                print(f" {agencia.id_agencia} - {agencia.nombre} - {agencia.app} - {agencia.apm} - {agencia.telefono} - {agencia.correo} - {agencia.empleados}")
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
        print("Error")
        print(e)

def insertar_agencia():
    print("INSERTAR UNA NUEVA AGENCIA")
    id_agencia = input("Escribe el ID de la agencia: ")
    agencia_nombre = input("Escribe el nombre de la agencia: ")
    nombre = input("Escribe el nombre: ")
    app = input("Escribe el apellido paterno: ")
    apm = input("Escribe el apellido materno: ")
    telefono = input("Escribe el teléfono: ")
    correo = input("Escribe el correo: ")
    empleados = input("Escribe el número de empleados: ")
    descripcion = input("Escribe la descripción: ")

    try:
        agencias_dao = AgenciaDAO()
        ultimo_id = agencias_dao.obtener_ultimo_id() + 1
        agencia = Agencia(id_agencia, agencia_nombre, nombre, app, apm, telefono, correo, empleados)
        agencias_dao.insertar(agencia)
        print("Inserción de la nueva agencia fue exitosa")
    except Exception as e:
        print("Error al insertar la agencia")
        print(e)

def actualizar_agencia():
    try:
        agencias_dao = AgenciaDAO()
        print("Lista de agencias disponibles")
        ver_agencia()
        id = int(input("Seleccione el id de la agencia a actualizar: "))
        agencia_nombre = input("Escribe el nombre de la agencia: ")
        nombre = input("Escribe el nombre: ")
        app = input("Escribe el apellido paterno: ")
        apm = input("Escribe el apellido materno: ")
        telefono = input("Escribe el teléfono: ")
        correo = input("Escribe el correo: ")
        empleados = input("Escribe el número de empleados: ")
        agencia = Agencia(id, agencia_nombre, nombre, app, apm, telefono, correo, empleados)
        agencias_dao.actualizar(agencia)
        print("La agencia fue actualizada con éxito")
    except Exception as e:
        print("Error al actualizar la agencia")
        print(e)

def eliminar_agencia():
    try:
        agencias_dao = AgenciaDAO()
        print("Lista de agencias disponibles")
        ver_agencia()
        id = int(input("Escriba el id de la agencia a eliminar: "))
        agencias_dao.eliminar(id)
        print(f"La agencia {id} ha sido eliminada con éxito")
    except Exception as e:
        print(f"Error al eliminar la agencia {id}")
        print(e)

#Cliente-------------------------------------------------------------------------
def ver_clientes():
    try:
        clientes_dao = ClienteDAO()
        clientes = clientes_dao.obtener_todo()

        if len(clientes) == 0:
            print("No hay clientes registrados")
        else:
            for cliente in clientes:
                print(f" {cliente.id_cliente} - {cliente.nombre} - {cliente.app} - {cliente.apm} - {cliente.telefono} - {cliente.correo} - {cliente.calle} - {cliente.colonia} - {cliente.numero_exterior}")
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
        print("Error")
        print(e)

def insertar_clientes():
    print("INSERTAR UN NUEVO CLIENTE")
    id_cliente = input("Escribe el ID del cliente: ")
    nombre = input("Escribe el nombre: ")
    app = input("Escribe el apellido paterno: ")
    apm = input("Escribe el apellido materno: ")
    telefono = input("Escribe el teléfono: ")
    correo = input("Escribe el correo: ")
    calle = input("Escribe la calle: ")
    colonia = input("Escribe la colonia: ")
    numero_exterior = input("Escribe el número exterior: ")

    try:
        clientes_dao = ClienteDAO()
        ultimo_id = clientes_dao.obtener_ultimo_id() + 1
        cliente = Cliente(id_cliente, nombre, app, apm, telefono, correo, calle, colonia, numero_exterior)
        clientes_dao.insertar(cliente)
        print("Inserción del nuevo cliente fue exitosa")
    except Exception as e:
        print("Error al insertar el cliente")
        print(e)

def actualizar_clientes():
    try:
        clientes_dao = ClienteDAO()
        print("Lista de clientes disponibles")
        ver_clientes()
        id = int(input("Seleccione el id del cliente a actualizar: "))
        nombre = input("Escribe el nombre: ")
        app = input("Escribe el apellido paterno: ")
        apm = input("Escribe el apellido materno: ")
        telefono = input("Escribe el teléfono: ")
        correo = input("Escribe el correo: ")
        calle = input("Escribe la calle: ")
        colonia = input("Escribe la colonia: ")
        numero_exterior = input("Escribe el número exterior: ")
        cliente = Cliente(id, nombre, app, apm, telefono, correo, calle, colonia, numero_exterior)
        clientes_dao.actualizar(cliente)
        print("El cliente fue actualizado con éxito")
    except Exception as e:
        print("Error al actualizar el cliente")
        print(e)

def eliminar_clientes():
    try:
        clientes_dao = ClienteDAO()
        print("Lista de clientes disponibles")
        ver_clientes()
        id = int(input("Escriba el id del cliente a eliminar: "))
        clientes_dao.eliminar(id)
        print(f"El cliente {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el cliente {id}")
        print(e)

#Contrato-------------------------------------------------------------------------
def ver_contratos():
    try:
        contratos_dao = ContratoDAO()
        contratos = contratos_dao.obtener_todo()

        if len(contratos) == 0:
            print("No hay contratos registrados")
        else:
            for contrato in contratos:
                print(f" {contrato.id_contrato} - {contrato.fecha_firma} - {contrato.costo} - {contrato.paquetes}")
        print("\n Conexion exitosa con la base de datos")
    except Exception as e:
        print("Error")
        print(e)

def insertar_contratos():
    print("INSERTAR UN NUEVO CONTRATO")
    id_contrato = input("Escribe el ID del contrato: ")
    fecha_firma = input("Escribe la fecha de firma: ")
    costo = float(input("Escribe el costo: "))
    paquetes = input("Escribe los paquetes: ")

    try:
        contratos_dao = ContratoDAO()
        ultimo_id = contratos_dao.obtener_ultimo_id() + 1
        contrato = Contrato(id_contrato, fecha_firma, costo, paquetes)
        contratos_dao.insertar(contrato)
        print("Inserción del nuevo contrato fue exitosa")
    except Exception as e:
        print("Error al insertar el contrato")
        print(e)

def actualizar_contratos():
    try:
        contratos_dao = ContratoDAO()
        print("Lista de contratos disponibles")
        ver_contratos()
        id = int(input("Seleccione el id del contrato a actualizar: "))
        fecha_firma = input("Escribe la fecha de firma: ")
        costo = float(input("Escribe el costo: "))
        paquetes = input("Escribe los paquetes: ")
        contrato = Contrato(id, fecha_firma, costo, paquetes)
        contratos_dao.actualizar(contrato)
        print("El contrato fue actualizado con éxito")
    except Exception as e:
        print("Error al actualizar el contrato")
        print(e)

def eliminar_contratos():
    try:
        contratos_dao = ContratoDAO()
        print("Lista de contratos disponibles")
        ver_contratos()
        id = int(input("Escriba el id del contrato a eliminar: "))
        contratos_dao.eliminar(id)
        print(f"El contrato {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el contrato {id}")
        print(e)

def menu_agencia():
    print("1. Ver todas las agencias")
    print("2. Insertar una nueva agencia")
    print("3. Actualizar una agencia existente")
    print("4. Eliminar una agencia existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_agencia()
        case 2:
            insertar_agencia()
        case 3:
            actualizar_agencia()
        case 4:
            eliminar_agencia()

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

def menu_clientes():
    print("1. Ver todos los clientes")
    print("2. Insertar un nuevo cliente")
    print("3. Actualizar un cliente existente")
    print("4. Eliminar un cliente existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_clientes()
        case 2:
            insertar_clientes()
        case 3:
            actualizar_clientes ()
        case 4:
            eliminar_clientes()

def menu_contratos():
    print("1. Ver todos los contratos")
    print("2. Insertar un nuevo contrato")
    print("3. Actualizar un contrato existente")
    print("4. Eliminar un contrato existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_contratos()
        case 2:
            insertar_contratos()
        case 3:
            actualizar_contratos()
        case 4:
            eliminar_contratos()
#ft.app(target=main_window)

def main():
    while True:
        print("=== Nova Estudio === ")
        print("Menú de opciones:")
        print("1. Inventario")
        print("2. Empleados")
        print("3. Eventos")
        print("4. Paquetes")
        print("5. Agencia")
        print("6. Clientes")    
        print("7. Contratos")
        print("8. Salir")
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
            menu_agencia()
        elif opcion == 6:
            menu_clientes()
        elif opcion == 7:
            menu_contratos()
        elif opcion == 8:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
   

if __name__ == "__main__":
    main()