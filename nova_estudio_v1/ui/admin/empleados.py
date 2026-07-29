import flet as ft

from dao.empleados_dao import EmpleadosDAO
from modelos.empleados import Empleados


def empleados(page: ft.Page):

    empleado_dao = EmpleadosDAO()

    empleado_seleccionado = None


    # =============================
    # CAMPOS DEL FORMULARIO
    # =============================

    txt_nombre = ft.TextField(
        label="Nombre",
        width=250
    )


    txt_app = ft.TextField(
        label="Apellido Paterno",
        width=250
    )


    txt_apm = ft.TextField(
        label="Apellido Materno",
        width=250
    )


    txt_puesto = ft.TextField(
        label="Puesto",
        width=250
    )


    txt_telefono = ft.TextField(
        label="Teléfono",
        width=250
    )


    txt_buscar = ft.TextField(
        label="Buscar empleado",
        prefix_icon=ft.Icons.SEARCH,
        expand=True
    )


    # =============================
    # TABLA EMPLEADOS
    # =============================

    tabla_empleados = ft.DataTable(

        columns=[

            ft.DataColumn(
                ft.Text("ID")
            ),

            ft.DataColumn(
                ft.Text("Nombre")
            ),

            ft.DataColumn(
                ft.Text("Puesto")
            ),

            ft.DataColumn(
                ft.Text("Teléfono")
            ),

            ft.DataColumn(
                ft.Text("Acciones")
            )

        ],

        rows=[]

    )

    # =============================
    # DIALOGO EMPLEADO
    # =============================

    dialogo = ft.AlertDialog(

        modal=True,

        title=ft.Text(
            "Nuevo Empleado"
        ),

        content=ft.Column(

            [

                txt_nombre,

                txt_app,

                txt_apm,

                txt_puesto,

                txt_telefono

            ],

            tight=True

        )

    )


    # =============================
    # CARGAR EMPLEADOS
    # =============================

    def cargar_empleados():

        tabla_empleados.rows.clear()

        try:

            lista_empleados = empleado_dao.obtener_todo()


            for empleado in lista_empleados:

                tabla_empleados.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                ft.Text(
                                    str(empleado.id_empleado)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    f"{empleado.nombre} {empleado.app} {empleado.apm}"
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    empleado.puesto
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    empleado.telefono
                                )
                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, emp=empleado:
                                                editar_empleado(emp)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, emp=empleado:
                                                eliminar_empleado(emp)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


            page.update()


        except Exception as error:

            mostrar_mensaje(
                f"Error al cargar empleados: {error}"
            )



    # =============================
    # LIMPIAR CAMPOS
    # =============================

    def limpiar_campos():

        txt_nombre.value = ""

        txt_app.value = ""

        txt_apm.value = ""

        txt_puesto.value = ""

        txt_telefono.value = ""

    # =============================
    # GUARDAR EMPLEADO
    # =============================

    def guardar_empleado(e):

        try:

            nuevo_id = empleado_dao.obtener_ultimo_id() + 1


            empleado = Empleados(

                nuevo_id,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_puesto.value,

                txt_telefono.value

            )


            empleado_dao.insertar(
                empleado
            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_empleados()


            mostrar_mensaje(
                "Empleado registrado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al guardar empleado: {error}"
            )



    # =============================
    # EDITAR EMPLEADO
    # =============================

    def editar_empleado(empleado):

        nonlocal empleado_seleccionado


        empleado_seleccionado = empleado


        txt_nombre.value = empleado.nombre

        txt_app.value = empleado.app

        txt_apm.value = empleado.apm

        txt_puesto.value = empleado.puesto

        txt_telefono.value = empleado.telefono


        dialogo.title = ft.Text(
            "Editar Empleado"
        )


        dialogo.actions = [

            ft.ElevatedButton(

                "Actualizar",

                icon=ft.Icons.SAVE,

                on_click=actualizar_empleado

            ),


            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            )

        ]


        dialogo.open = True

        page.update()



    # =============================
    # ACTUALIZAR EMPLEADO
    # =============================

    def actualizar_empleado(e):

        try:

            empleado_actualizado = Empleados(

                empleado_seleccionado.id_empleado,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_puesto.value,

                txt_telefono.value

            )


            empleado_dao.actualizar(
                empleado_actualizado
            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_empleados()


            mostrar_mensaje(
                "Empleado actualizado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al actualizar empleado: {error}"
            )

    # =============================
    # ELIMINAR EMPLEADO
    # =============================

    def eliminar_empleado(empleado):

        try:

            empleado_dao.eliminar(
                empleado.id_empleado
            )


            cargar_empleados()


            mostrar_mensaje(
                "Empleado eliminado correctamente."
            )


        except Exception as error:

            mostrar_mensaje(
                f"Error al eliminar empleado: {error}"
            )



    # =============================
    # BUSCAR EMPLEADOS
    # =============================

    def buscar_empleados(e):

        texto = txt_buscar.value.lower()

        tabla_empleados.rows.clear()


        for empleado in empleado_dao.obtener_todo():

            nombre_completo = (

                f"{empleado.nombre} "
                f"{empleado.app} "
                f"{empleado.apm}"

            ).lower()


            if (

                texto in nombre_completo

                or texto in empleado.puesto.lower()

                or texto in empleado.telefono.lower()

            ):

                tabla_empleados.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(
                                ft.Text(
                                    str(empleado.id_empleado)
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    f"{empleado.nombre} {empleado.app} {empleado.apm}"
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    empleado.puesto
                                )
                            ),


                            ft.DataCell(
                                ft.Text(
                                    empleado.telefono
                                )
                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, emp=empleado:
                                                editar_empleado(emp)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, emp=empleado:
                                                eliminar_empleado(emp)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


        page.update()



    # =============================
    # NUEVO EMPLEADO
    # =============================

    def nuevo_empleado(e):

        limpiar_campos()


        dialogo.title = ft.Text(
            "Nuevo Empleado"
        )


        dialogo.actions = [

            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            ),


            ft.ElevatedButton(

                "Guardar",

                icon=ft.Icons.SAVE,

                on_click=guardar_empleado

            )

        ]


        page.dialog = dialogo

        dialogo.open = True

        page.update()



    # =============================
    # CERRAR DIALOGO
    # =============================

    def cerrar_dialogo():

        dialogo.open = False

        page.update()



    # =============================
    # MENSAJES
    # =============================

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )

        page.snack_bar.open = True

        page.update()



    txt_buscar.on_change = buscar_empleados


    cargar_empleados()



    # =============================
    # INTERFAZ FINAL
    # =============================

    return ft.Container(

        expand=True,

        padding=20,

        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Gestión de Empleados",

                            size=28,

                            weight=ft.FontWeight.BOLD

                        ),


                        ft.Container(

                            expand=True

                        ),


                        ft.ElevatedButton(

                            "Nuevo Empleado",

                            icon=ft.Icons.ADD,

                            on_click=nuevo_empleado

                        )

                    ]

                ),


                txt_buscar,


                ft.Container(

                    expand=True,

                    content=tabla_empleados

                )

            ],

            expand=True

        )

    )