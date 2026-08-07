import flet as ft

from dao.inventario_dao import InventarioDAO
from modelos.inventario import Inventario

def inventario(page: ft.Page):
    dao = InventarioDAO()

    inventario_actual = None

    # campos del formulario

    nombre = ft.TextField(
        label="Nombre",
        width=250
    )

    tipo = ft.TextField(
        label="Tipo",
        width=250
    )

    estado = ft.TextField(
        label="Estado",
        width=250
    )

    cantidad = ft.TextField(
        label="Cantidad",
        width=250
    )

    disponible = ft.Dropdown(
        label="Disponible",

        width=250,

        options=[
            ft.dropdown.Option(
                "True"
            ),

            ft.dropdown.Option(
                "False"
            )
        ]
    )

    formulario = ft.Container(
        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15
    )

    # tabla inventario

    tabla = ft.DataTable(
        expand=True,

        column_spacing=45,

        horizontal_margin=30,

        columns=[
            ft.DataColumn(
                ft.Text("ID")
            ),

            ft.DataColumn(
                ft.Text("Nombre")
            ),

            ft.DataColumn(
                ft.Text("Tipo")
            ),

            ft.DataColumn(
                ft.Text("Estado")
            ),

            ft.DataColumn(
                ft.Text("Cantidad")
            ),

            ft.DataColumn(
                ft.Text("Disponible")
            ),

            ft.DataColumn(
                ft.Text("Acciones")
            )

        ],

        rows=[]
    )

    def limpiar():
        nombre.value = ""

        tipo.value = ""

        estado.value = ""

        cantidad.value = ""

        disponible.value = None

    # cargar tabla

    def cargar():
        tabla.rows.clear()

        inventarios_lista = dao.obtener_todo()

        for item in inventarios_lista:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(
                                str(item.id_inventario)
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                item.nombre
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                item.tipo
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                item.estado
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(item.cantidad)
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                "Disponible"
                                if item.disponible
                                else
                                "No disponible"
                            )
                        ),

                        ft.DataCell(
                            ft.Container(
                                width=130,

                                content=ft.Row(
                                    [
                                        ft.IconButton(
                                            icon=ft.Icons.EDIT,

                                            icon_color=ft.Colors.BLUE_400,

                                            tooltip="Editar inventario",

                                            on_click=lambda e, inv=item: editar(inv)
                                        ),

                                        ft.IconButton(
                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar inventario",

                                            on_click=lambda e, inv=item: eliminar(inv)
                                        )

                                    ],

                                    spacing=8
                                )
                            )
                        )

                    ]
                )
            )

        page.update()

    # mostrar formulario

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

                        tipo
                    ]
                ),

                ft.Row(
                    [
                        estado,

                        cantidad
                    ]
                ),

                ft.Row(
                    [
                        disponible
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

    # cerrar formulario

    def cerrar_formulario(e=None):
        formulario.visible = False

        limpiar()

        page.update()

    # nuevo inventario

    def nuevo_inventario(e):
        nonlocal inventario_actual

        inventario_actual = None

        limpiar()

        mostrar_formulario(
            "Nuevo Inventario"
        )

    # guardar inventario

    def guardar(e):
        try:
            nuevo = Inventario(
                id_inventario=dao.obtener_ultimo_id()+1,

                nombre=nombre.value,

                tipo=tipo.value,

                estado=estado.value,

                cantidad=int(
                    cantidad.value

                    if cantidad.value

                    else 0
                ),

                disponible=True

                if disponible.value == "True"

                else False
            )

            dao.insertar(nuevo)

            cerrar_formulario()

            cargar()

            mostrar_mensaje(
                "Inventario agregado correctamente"
            )

        except Exception as error:
            mostrar_mensaje(
                f"Error: {error}"
            )

    # editar inventario

    def editar(item):
        nonlocal inventario_actual

        inventario_actual = item

        nombre.value = item.nombre

        tipo.value = item.tipo

        estado.value = item.estado

        cantidad.value = str(
            item.cantidad
        )

        disponible.value = (
            "True"

            if item.disponible

            else

            "False"
        )

        mostrar_formulario(
            "Editar Inventario"
        )

        formulario.content.controls[-1].controls[0].text = "Actualizar"

        formulario.content.controls[-1].controls[0].on_click = actualizar

        page.update()

    # actualizar inventario

    def actualizar(e):
        try:
            inventario_actual.nombre = nombre.value

            inventario_actual.tipo = tipo.value

            inventario_actual.estado = estado.value

            inventario_actual.cantidad = int(
                cantidad.value

                if cantidad.value

                else 0
            )

            inventario_actual.disponible = (
                True

                if disponible.value == "True"

                else False
            )

            dao.actualizar(
                inventario_actual
            )

            cerrar_formulario()

            cargar()

            mostrar_mensaje(
                "Inventario actualizado correctamente"
            )

        except Exception as error:
            mostrar_mensaje(
                f"Error al actualizar: {error}"
            )

    # mensajes

    def mostrar_mensaje(texto):
        page.snack_bar = ft.SnackBar(
            ft.Text(texto)
        )

        page.snack_bar.open = True

        page.update()

    # eliminar inventario
    # ==========================

    def eliminar(item):
        print(
            "BOTON ELIMINAR INVENTARIO:",
            item.id_inventario
        )

        def aceptar(e):
            try:
                print(
                    "ELIMINANDO INVENTARIO:",
                    item.id_inventario
                )

                dao.eliminar(
                    item.id_inventario
                )

                dialogo_eliminar.open = False

                page.update()

                cargar()

                mostrar_mensaje(
                    "Inventario eliminado correctamente"
                )

            except Exception as error:
                print(
                    "ERROR AL ELIMINAR INVENTARIO:",
                    error
                )

                mostrar_mensaje(
                    f"Error al eliminar: {error}"
                )

        def cancelar(e):
            dialogo_eliminar.open = False

            page.update()

        dialogo_eliminar = ft.AlertDialog(
            modal=True,

            title=ft.Text(
                "Eliminar inventario"
            ),

            content=ft.Text(
                f"¿Seguro que deseas eliminar {item.nombre}?"
            ),

            actions=[
                ft.TextButton(
                    "Cancelar",

                    on_click=cancelar
                ),

                ft.TextButton(
                    "Eliminar",

                    icon=ft.Icons.DELETE,

                    on_click=aceptar
                )
            ]
        )

        page.overlay.append(dialogo_eliminar)

        dialogo_eliminar.open = True

        page.update()

    # botón nuevo inventario

    boton_nuevo = ft.ElevatedButton(
        "Nuevo Inventario",

        icon=ft.Icons.ADD,

        on_click=nuevo_inventario
    )

    # cargar datos iniciales

    cargar()

    # interfaz final

    return ft.Container(
        expand=True,

        padding=20,

        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Gestión de Inventario",

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
                    height=0
                ),

                ft.Container(
                    padding=0,

                    content=ft.Column(
                        [
                            tabla
                        ],

                        spacing=0
                    )
                )
            ],

            expand=True,

            spacing=0
        )
    )
