import flet as ft

from dao.paquetes_dao import PaquetesDAO
from modelos.paquetes import Paquetes

def paquetes(page: ft.Page):
    dao = PaquetesDAO()

    paquete_actual = None

    # campos del formulario

    nombre = ft.TextField(
        label="Nombre del Paquete",

        width=250
    )

    tipo_paquete = ft.TextField(
        label="Tipo de Paquete",

        width=250
    )

    costo = ft.TextField(
        label="Costo",

        width=250
    )

    descripcion = ft.TextField(
        label="Descripción",

        width=250,

        multiline=True
    )

    formulario = ft.Container(
        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15
    )

    # tabla paquetes

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
                ft.Text("Tipo Paquete")
            ),

            ft.DataColumn(
                ft.Text("Costo")
            ),

            ft.DataColumn(
                ft.Text("Descripción")
            ),

            ft.DataColumn(
                ft.Text("Acciones")
            )

        ],

        rows=[]
    )

    def limpiar():
        nombre.value = ""

        tipo_paquete.value = ""

        costo.value = ""

        descripcion.value = ""

    # cargar tabla

    def cargar():
        tabla.rows.clear()

        paquetes_lista = dao.obtener_todo()

        for paquete in paquetes_lista:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(
                                str(paquete.id_paquetes)
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                paquete.nombre
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                paquete.tipo_paquete
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                str(paquete.costo)
                            )
                        ),

                        ft.DataCell(
                            ft.Text(
                                paquete.descripcion
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

                                            tooltip="Editar paquete",

                                            on_click=lambda e, p=paquete: editar(p)
                                        ),

                                        ft.IconButton(
                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar paquete",

                                            on_click=lambda e, p=paquete: eliminar(p)
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

                        tipo_paquete
                    ]
                ),

                ft.Row(
                    [
                        costo
                    ]
                ),

                descripcion,

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

    # nuevo paquete

    def nuevo_paquete(e):
        nonlocal paquete_actual

        paquete_actual = None

        limpiar()

        mostrar_formulario(
            "Nuevo Paquete"
        )

    # guardar paquete

    def guardar(e):
        try:
            nuevo = Paquetes(
                id_paquetes=dao.obtener_ultimo_id()+1,

                nombre=nombre.value,

                tipo_paquete=tipo_paquete.value,

                costo=float(
                    costo.value

                    if costo.value

                    else 0
                ),

                descripcion=descripcion.value
            )

            dao.insertar(nuevo)

            cerrar_formulario()

            cargar()

            mostrar_mensaje(
                "Paquete agregado correctamente"
            )

        except Exception as error:
            mostrar_mensaje(
                f"Error: {error}"
            )

    # editar paquete

    def editar(paquete):
        nonlocal paquete_actual

        paquete_actual = paquete

        nombre.value = paquete.nombre

        tipo_paquete.value = paquete.tipo_paquete

        costo.value = str(
            paquete.costo
        )

        descripcion.value = paquete.descripcion

        mostrar_formulario(
            "Editar Paquete"
        )

        formulario.content.controls[-1].controls[0].text = "Actualizar"

        formulario.content.controls[-1].controls[0].on_click = actualizar

        page.update()

    # actualizar paquete

    def actualizar(e):
        try:
            paquete_actual.nombre = nombre.value

            paquete_actual.tipo_paquete = tipo_paquete.value

            paquete_actual.costo = float(
                costo.value

                if costo.value

                else 0
            )

            paquete_actual.descripcion = descripcion.value

            dao.actualizar(
                paquete_actual
            )

            cerrar_formulario()

            cargar()

            mostrar_mensaje(
                "Paquete actualizado correctamente"
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

    # eliminar paquete

    def eliminar(paquete):
        print(
            "BOTON ELIMINAR PAQUETE:",
            paquete.id_paquetes
        )

        def aceptar(e):
            try:
                print(
                    "ELIMINANDO PAQUETE:",
                    paquete.id_paquetes
                )

                dao.eliminar(
                    paquete.id_paquetes
                )

                dialogo_eliminar.open = False

                page.update()

                cargar()

                mostrar_mensaje(
                    "Paquete eliminado correctamente"
                )

            except Exception as error:
                print(
                    "ERROR AL ELIMINAR PAQUETE:",
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
                "Eliminar paquete"
            ),

            content=ft.Text(
                f"¿Seguro que deseas eliminar {paquete.nombre}?"
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

    # botón nuevo paquete

    boton_nuevo = ft.ElevatedButton(
        "Nuevo Paquete",

        icon=ft.Icons.ADD,

        on_click=nuevo_paquete
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
                            "Gestión de Paquetes",

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
