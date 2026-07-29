import flet as ft

from dao.dj_dao import DjDAO
from modelos.dj import Dj


def djs(page: ft.Page):

    dj_dao = DjDAO()

    dj_seleccionado = None


    # CAMPOS DEL FORMULARIO

    txt_nombre = ft.TextField(

        label="Nombre",

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


    txt_especialidad = ft.TextField(

        label="Especialidad",

        width=250

    )


    txt_disponibilidad = ft.Dropdown(

        label="Disponibilidad",

        width=250,

        options=[

            ft.dropdown.Option("True"),

            ft.dropdown.Option("False")

        ]

    )


    txt_buscar = ft.TextField(

        label="Buscar DJ",

        prefix_icon=ft.Icons.SEARCH,

        expand=True

    )



    # TABLA DJs

    tabla_djs = ft.DataTable(

        columns=[

            ft.DataColumn(
                ft.Text("ID")
            ),

            ft.DataColumn(
                ft.Text("Nombre")
            ),

            ft.DataColumn(
                ft.Text("Apellido")
            ),

            ft.DataColumn(
                ft.Text("Teléfono")
            ),

            ft.DataColumn(
                ft.Text("Especialidad")
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

    # DIALOGO DJ

    dialogo = ft.AlertDialog(

        modal=True,

        title=ft.Text(
            "Nuevo DJ"
        ),

        content=ft.Column(

            [

                txt_nombre,

                txt_app,

                txt_apm,

                txt_telefono,

                txt_especialidad,

                txt_disponibilidad

            ],

            tight=True

        )

    )



    # CARGAR DJs

    def cargar_djs():

        tabla_djs.rows.clear()


        try:

            lista_djs = dj_dao.obtener_todo()


            for dj in lista_djs:


                tabla_djs.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(

                                ft.Text(
                                    str(dj.id_dj)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.nombre
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.app + " " + dj.apm
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.telefono
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.especialidad
                                )

                            ),


                            ft.DataCell(

                                ft.Text(

                                    "Disponible"
                                    if dj.disponibilidad
                                    else "No disponible"

                                )

                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, d=dj:
                                                editar_dj(d)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, d=dj:
                                                eliminar_dj(d)

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

                f"Error al cargar DJs: {error}"

            )



    # LIMPIAR CAMPOS

    def limpiar_campos():

        txt_nombre.value = ""

        txt_app.value = ""

        txt_apm.value = ""

        txt_telefono.value = ""

        txt_especialidad.value = ""

        txt_disponibilidad.value = None 


    # GUARDAR DJ

    def guardar_dj(e):

        try:

            nuevo_id = dj_dao.obtener_ultimo_id() + 1


            disponibilidad = True

            if txt_disponibilidad.value == "False":

                disponibilidad = False



            nuevo_dj = Dj(

                nuevo_id,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_telefono.value,

                txt_especialidad.value,

                disponibilidad

            )


            dj_dao.insertar(

                nuevo_dj

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_djs()


            mostrar_mensaje(

                "DJ registrado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al guardar DJ: {error}"

            )



    # EDITAR DJ

    def editar_dj(dj):

        nonlocal dj_seleccionado


        dj_seleccionado = dj


        txt_nombre.value = dj.nombre

        txt_app.value = dj.app

        txt_apm.value = dj.apm

        txt_telefono.value = dj.telefono

        txt_especialidad.value = dj.especialidad

        txt_disponibilidad.value = str(dj.disponibilidad)



        dialogo.title = ft.Text(

            "Editar DJ"

        )


        dialogo.actions = [

            ft.ElevatedButton(

                "Actualizar",

                icon=ft.Icons.SAVE,

                on_click=actualizar_dj

            ),


            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            )

        ]


        dialogo.open = True

        page.update()



    # ACTUALIZAR DJ

    def actualizar_dj(e):

        try:

            disponibilidad = True


            if txt_disponibilidad.value == "False":

                disponibilidad = False



            dj_actualizado = Dj(

                dj_seleccionado.id_dj,

                txt_nombre.value,

                txt_app.value,

                txt_apm.value,

                txt_telefono.value,

                txt_especialidad.value,

                disponibilidad

            )


            dj_dao.actualizar(

                dj_actualizado

            )


            cerrar_dialogo()

            limpiar_campos()

            cargar_djs()


            mostrar_mensaje(

                "DJ actualizado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al actualizar DJ: {error}"

            ) 

    # ELIMINAR DJ

    def eliminar_dj(dj):

        try:

            dj_dao.eliminar(

                dj.id_dj

            )


            cargar_djs()


            mostrar_mensaje(

                "DJ eliminado correctamente."

            )


        except Exception as error:

            mostrar_mensaje(

                f"Error al eliminar DJ: {error}"

            )



    # BUSCAR DJ

    def buscar_djs(e):

        texto = txt_buscar.value.lower()


        tabla_djs.rows.clear()


        for dj in dj_dao.obtener_todo():


            if texto in dj.nombre.lower() or texto in dj.especialidad.lower():


                tabla_djs.rows.append(

                    ft.DataRow(

                        cells=[

                            ft.DataCell(

                                ft.Text(
                                    str(dj.id_dj)
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.nombre
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.app + " " + dj.apm
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.telefono
                                )

                            ),


                            ft.DataCell(

                                ft.Text(
                                    dj.especialidad
                                )

                            ),


                            ft.DataCell(

                                ft.Text(

                                    "Disponible"
                                    if dj.disponibilidad
                                    else "No disponible"

                                )

                            ),


                            ft.DataCell(

                                ft.Row(

                                    [

                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            tooltip="Editar",

                                            on_click=lambda e, d=dj:
                                                editar_dj(d)

                                        ),


                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            tooltip="Eliminar",

                                            icon_color=ft.Colors.RED,

                                            on_click=lambda e, d=dj:
                                                eliminar_dj(d)

                                        )

                                    ]

                                )

                            )

                        ]

                    )

                )


        page.update()



    # NUEVO DJ

    def nuevo_dj(e):

        limpiar_campos()


        dialogo.title = ft.Text(

            "Nuevo DJ"

        )


        dialogo.actions = [

            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar_dialogo()

            ),


            ft.ElevatedButton(

                "Guardar",

                icon=ft.Icons.SAVE,

                on_click=guardar_dj

            )

        ]


        page.dialog = dialogo


        dialogo.open = True


        page.update()



    # CERRAR DIALOGO


    def cerrar_dialogo():

        dialogo.open = False

        page.update()



    # MENSAJES

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )

        page.snack_bar.open = True

        page.update()



    txt_buscar.on_change = buscar_djs


    cargar_djs()



    # INTERFAZ FINAL

    return ft.Container(

        expand=True,

        padding=20,

        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Gestión de DJs",

                            size=28,

                            weight=ft.FontWeight.BOLD

                        ),


                        ft.Container(

                            expand=True

                        ),


                        ft.ElevatedButton(

                            "Nuevo DJ",

                            icon=ft.Icons.ADD,

                            on_click=nuevo_dj

                        )

                    ]

                ),


                txt_buscar,


                ft.Container(

                    expand=True,

                    content=tabla_djs

                )

            ],

            expand=True

        )

    )