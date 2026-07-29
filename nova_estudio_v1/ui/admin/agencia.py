import flet as ft

from dao.agencia_dao import AgenciaDAO
from modelos.agencia import Agencia


def agencia(page: ft.Page):

    agencia_dao = AgenciaDAO()

    agencia_seleccionada = None


    # =============================
    # CAMPOS DEL FORMULARIO
    # =============================

    txt_agencia_nombre = ft.TextField(

        label="Nombre de la agencia",

        width=250

    )


    txt_nombre = ft.TextField(

        label="Nombre responsable",

        width=250

    )


    txt_app = ft.TextField(

        label="Apellido paterno",

        width=250

    )


    txt_apm = ft.TextField(

        label="Apellido materno",

        width=250

    )


    txt_telefono = ft.TextField(

        label="Teléfono",

        width=250

    )


    txt_correo = ft.TextField(

        label="Correo",

        width=250

    )


    txt_empleados = ft.TextField(

        label="Empleados",

        width=250

    )


    txt_buscar = ft.TextField(

        label="Buscar agencia",

        prefix_icon=ft.Icons.SEARCH,

        expand=True

    )



    # =============================
    # TABLA AGENCIA
    # =============================

    tabla_agencia = ft.DataTable(

        columns=[

            ft.DataColumn(
                ft.Text("ID")
            ),

            ft.DataColumn(
                ft.Text("Agencia")
            ),

            ft.DataColumn(
                ft.Text("Responsable")
            ),

            ft.DataColumn(
                ft.Text("Teléfono")
            ),

            ft.DataColumn(
                ft.Text("Correo")
            ),

            ft.DataColumn(
                ft.Text("Acciones")
            )

        ],

        rows=[]

    ) 

    # =============================
    # DIALOGO AGENCIA
    # =============================

    dialogo = ft.AlertDialog(

        modal=True,

        title=ft.Text(
            "Nueva Agencia"
        ),

        content=ft.Column(

            [

                txt_agencia_nombre,

                txt_nombre,

                txt_app,

                txt_apm,

                txt_telefono,

                txt_correo,

                txt_empleados

            ],

            tight=True

        )

    )



    # =============================
    # CARGAR AGENCIA
    # =============================

    def cargar_agencia():

        tabla_agencia.rows.clear()

        try:

            lista_agencias = agencia_dao.obtener_todo()


            for item in lista_agencias:

                tabla_agencia.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(

                                ft.Text(
                                    str(item.id_agencia)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.agencia_nombre
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.nombre + " " + item.app
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.telefono
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.correo
                                )

                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, a=item:
                                                editar_agencia(a)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, a=item:
                                                eliminar_agencia(a)

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

                f"Error al cargar agencia: {error}"

            )



    # =============================
    # LIMPIAR CAMPOS
    # =============================

    def limpiar_campos():

        txt_agencia_nombre.value = ""

        txt_nombre.value = ""

        txt_app.value = ""

        txt_apm.value = ""

        txt_telefono.value = ""

        txt_correo.value = ""

        txt_empleados.value = "" 

    # =============================
    # GUARDAR AGENCIA
    # =============================

    def guardar_agencia(e):

        try:

            nuevo_id = agencia_dao.obtener_ultimo_id() + 1


            nueva_agencia = Agencia(

                nuevo_id,

                txt_agencia_nombre.value,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_telefono.value,

                txt_correo.value,

                txt_empleados.value

            )


            agencia_dao.insertar(

                nueva_agencia

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_agencia()


            mostrar_mensaje(

                "Agencia registrada correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al guardar agencia: {error}"

            )



    # =============================
    # EDITAR AGENCIA
    # =============================

    def editar_agencia(item):

        nonlocal agencia_seleccionada


        agencia_seleccionada = item


        txt_agencia_nombre.value = item.agencia_nombre

        txt_nombre.value = item.nombre

        txt_app.value = item.app

        txt_apm.value = item.apm

        txt_telefono.value = item.telefono

        txt_correo.value = item.correo

        txt_empleados.value = str(item.empleados)


        dialogo.title = ft.Text(

            "Editar Agencia"

        )


        dialogo.actions = [

            ft.ElevatedButton(

                "Actualizar",

                icon=ft.Icons.SAVE,

                on_click=actualizar_agencia

            ),


            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            )

        ]


        dialogo.open = True

        page.update()



    # =============================
    # ACTUALIZAR AGENCIA
    # =============================

    def actualizar_agencia(e):

        try:

            agencia_actualizada = Agencia(

                agencia_seleccionada.id_agencia,

                txt_agencia_nombre.value,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_telefono.value,

                txt_correo.value,

                txt_empleados.value

            )


            agencia_dao.actualizar(

                agencia_actualizada

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_agencia()


            mostrar_mensaje(

                "Agencia actualizada correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al actualizar agencia: {error}"

            ) 

    # =============================
    # ELIMINAR AGENCIA
    # =============================

    def eliminar_agencia(item):

        try:

            agencia_dao.eliminar(

                item.id_agencia

            )


            cargar_agencia()


            mostrar_mensaje(

                "Agencia eliminada correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al eliminar agencia: {error}"

            )



    # =============================
    # BUSCAR AGENCIA
    # =============================

    def buscar_agencia(e):

        texto = txt_buscar.value.lower()


        tabla_agencia.rows.clear()


        for item in agencia_dao.obtener_todo():


            if texto in item.agencia_nombre.lower() or texto in item.correo.lower():


                tabla_agencia.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(

                                ft.Text(
                                    str(item.id_agencia)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.agencia_nombre
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.nombre + " " + item.app
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.telefono
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    item.correo
                                )

                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, a=item:
                                                editar_agencia(a)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, a=item:
                                                eliminar_agencia(a)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


        page.update()



    # =============================
    # NUEVA AGENCIA
    # =============================

    def nueva_agencia(e):

        limpiar_campos()


        dialogo.title = ft.Text(

            "Nueva Agencia"

        )


        dialogo.actions = [

            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            ),


            ft.ElevatedButton(

                "Guardar",

                icon=ft.Icons.SAVE,

                on_click=guardar_agencia

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



    txt_buscar.on_change = buscar_agencia


    cargar_agencia()



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

                            "Gestión de Agencia",

                            size=28,

                            weight=ft.FontWeight.BOLD

                        ),


                        ft.Container(

                            expand=True

                        ),


                        ft.ElevatedButton(

                            "Nueva Agencia",

                            icon=ft.Icons.ADD,

                            on_click=nueva_agencia

                        )

                    ]

                ),


                txt_buscar,


                ft.Container(

                    expand=True,

                    content=tabla_agencia

                )

            ],

            expand=True

        )

    )