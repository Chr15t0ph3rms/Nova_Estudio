import flet as ft

from dao.cliente_dao import ClienteDAO
from modelos.cliente import Cliente

def clientes(page: ft.Page):
    dao = ClienteDAO()

    cliente_actual = None

    # campos

    nombre = ft.TextField(
        label="Nombre",
        width=250
    )

    app = ft.TextField(
        label="Apellido Paterno",
        width=250
    )

    apm = ft.TextField(
        label="Apellido Materno",
        width=250
    )

    telefono = ft.TextField(
        label="Teléfono",
        width=250
    )

    correo = ft.TextField(
        label="Correo",
        width=250
    )

    calle = ft.TextField(
        label="Calle",
        width=250
    )

    numero_exterior = ft.TextField(
        label="Número Exterior",
        width=250
    )

    colonia = ft.TextField(
        label="Colonia",
        width=250
    )

    formulario = ft.Container(
        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15
    )

    # tabla

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),

            ft.DataColumn(ft.Text("Nombre")),

            ft.DataColumn(ft.Text("Apellido P.")),

            ft.DataColumn(ft.Text("Apellido M.")),

            ft.DataColumn(ft.Text("Teléfono")),

            ft.DataColumn(ft.Text("Correo")),

            ft.DataColumn(ft.Text("Calle")),

            ft.DataColumn(ft.Text("Número")),

            ft.DataColumn(ft.Text("Colonia")),

            ft.DataColumn(ft.Text("Acciones"))
        ],

        rows=[]
    )

    def limpiar():
        nombre.value = ""

        app.value = ""

        apm.value = ""

        telefono.value = ""

        correo.value = ""

        calle.value = ""

        numero_exterior.value = ""

        colonia.value = ""

    # cargar datos

    def cargar():
        tabla.rows.clear()

        lista = dao.obtener_todos()

        for cliente in lista:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(str(cliente.id_cliente))
                        ),

                        ft.DataCell(
                            ft.Text(cliente.nombre)
                        ),

                        ft.DataCell(
                            ft.Text(cliente.app)
                        ),

                        ft.DataCell(
                            ft.Text(cliente.apm)
                        ),

                        ft.DataCell(
                            ft.Text(cliente.telefono)
                        ),

                        ft.DataCell(
                            ft.Text(cliente.correo)
                        ),

                        ft.DataCell(
                            ft.Text(cliente.calle)
                        ),

                        ft.DataCell(
                            ft.Text(str(cliente.numero_exterior))
                        ),

                        ft.DataCell(
                            ft.Text(cliente.colonia)
                        ),

                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,

                                        icon_color=ft.Colors.BLUE,

                                        on_click=lambda e,c=cliente:
                                        editar(c)
                                    ),

                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,

                                        icon_color=ft.Colors.RED,

                                        on_click=lambda e,c=cliente:
                                        eliminar(c)
                                    )

                                ]
                            )
                        )

                    ]
                )
            )

        page.update()

    # formulario

    def mostrar_formulario(titulo):
        formulario.content = ft.Column(
            [
                ft.Text(
                    titulo,

                    size=25,

                    weight=ft.FontWeight.BOLD,

                    color=ft.Colors.WHITE
                ),

                ft.Row(
                    [
                        nombre,
                        app
                    ]
                ),

                ft.Row(
                    [
                        apm,
                        telefono
                    ]
                ),

                ft.Row(
                    [
                        correo,
                        calle
                    ]
                ),

                ft.Row(
                    [
                        numero_exterior,
                        colonia
                    ]
                ),

                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Guardar",

                            icon=ft.Icons.SAVE,

                            on_click=guardar
                        ),

                        ft.TextButton(
                            "Cancelar",

                            on_click=cerrar_formulario
                        )
                    ]
                )
            ]
        )

        formulario.visible = True

        page.update()

    def cerrar_formulario(e=None):
        formulario.visible = False

        limpiar()

        page.update()

    # nuevo

    def nuevo_cliente(e):
        nonlocal cliente_actual

        cliente_actual = None

        limpiar()

        mostrar_formulario(
            "Nuevo Cliente"
        )

    # guardar cliente

    def guardar(e):
        try:
            nuevo = Cliente(
                id_cliente=dao.obtener_ultimo_id()+1,

                nombre=nombre.value,

                app=app.value,

                apm=apm.value,

                telefono=telefono.value,

                correo=correo.value,

                calle=calle.value,

                numero_exterior=int(
                    numero_exterior.value
                    if numero_exterior.value
                    else 0
                ),

                colonia=colonia.value
            )

            dao.insertar(nuevo)

            cerrar_formulario()

            cargar()

            mostrar_mensaje(
                "Cliente agregado correctamente"
            )

        except Exception as error:
            mostrar_mensaje(
                f"Error: {error}"
            )

    # editar cliente

    def editar(cliente):
        nonlocal cliente_actual

        cliente_actual = cliente

        nombre.value = cliente.nombre

        app.value = cliente.app

        apm.value = cliente.apm

        telefono.value = cliente.telefono

        correo.value = cliente.correo

        calle.value = cliente.calle

        numero_exterior.value = str(
            cliente.numero_exterior
        )

        colonia.value = cliente.colonia

        mostrar_formulario(
            "Editar Cliente"
        )

    # actualizar cliente

    def actualizar(e):
        try:
            cliente_actual.nombre = nombre.value

            cliente_actual.app = app.value

            cliente_actual.apm = apm.value

            cliente_actual.telefono = telefono.value

            cliente_actual.correo = correo.value

            cliente_actual.calle = calle.value

            cliente_actual.numero_exterior = int(
                numero_exterior.value
                if numero_exterior.value
                else 0
            )

            cliente_actual.colonia = colonia.value

            dao.actualizar(
                cliente_actual
            )

            cerrar_formulario()

            cargar()

            mostrar_mensaje(
                "Cliente actualizado correctamente"
            )

        except Exception as error:
            mostrar_mensaje(
                f"Error al actualizar: {error}"
            )

    # mensajes

    def mostrar_mensaje(texto):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto)
        )

        page.snack_bar.open = True

        page.update()

    # eliminar cliente

    def eliminar(cliente):
        print(
            "BOTON ELIMINAR CLIENTE:",
            cliente.id_cliente
        )

        def confirmar(e):
            try:
                print(
                    "ELIMINANDO CLIENTE:",
                    cliente.id_cliente
                )

                dao.eliminar(
                    cliente.id_cliente
                )

                dialogo.open = False

                page.update()

                cargar()

                mostrar_mensaje(
                    "Cliente eliminado correctamente"
                )

            except Exception as error:
                print(
                    "ERROR AL ELIMINAR CLIENTE:",
                    error
                )

                mostrar_mensaje(
                    f"Error al eliminar: {error}"
                )

        def cancelar(e):
            dialogo.open = False

            page.update()

        dialogo = ft.AlertDialog(
            modal=True,

            title=ft.Text(
                "Eliminar cliente"
            ),

            content=ft.Text(
                f"¿Seguro que deseas eliminar a {cliente.nombre}?"
            ),

            actions=[
                ft.TextButton(
                    "Cancelar",

                    on_click=cancelar
                ),

                ft.TextButton(
                    "Eliminar",

                    icon=ft.Icons.DELETE,

                    on_click=confirmar
                )
            ]
        )

        page.overlay.append(dialogo)

        dialogo.open = True

        page.update()

    # botón nuevo

    boton_nuevo = ft.ElevatedButton(
        "Nuevo Cliente",

        icon=ft.Icons.ADD,

        on_click=nuevo_cliente
    )

    # inicio

    cargar()

    return ft.Container(
        expand=True,

        padding=20,

        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Gestión de Clientes",

                            size=30,

                            weight=ft.FontWeight.BOLD,

                            color=ft.Colors.WHITE
                        ),

                        ft.Container(
                            expand=True
                        ),

                        boton_nuevo
                    ]
                ),

                ft.Divider(),

                formulario,

                ft.Container(
                    expand=True,

                    content=tabla
                )
            ],

            expand=True
        )
    )
