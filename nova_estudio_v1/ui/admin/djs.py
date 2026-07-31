import flet as ft

from dao.dj_dao import DjDAO
from modelos.dj import Dj



def djs(page: ft.Page):


    dao = DjDAO()

    dj_actual = None



    # ==========================
    # CAMPOS DEL FORMULARIO
    # ==========================


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


    especialidad = ft.TextField(
        label="Especialidad",
        width=250
    )


    disponibilidad = ft.Dropdown(

        label="Disponibilidad",

        width=250,

        options=[

            ft.dropdown.Option(
                "Disponible"
            ),

            ft.dropdown.Option(
                "No disponible"
            )

        ]

    )



    formulario = ft.Container(

        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15

    )



    # ==========================
    # TABLA DJs
    # ==========================


    tabla = ft.DataTable(

        expand=True,

        column_spacing=35,

        horizontal_margin=30,


        columns=[


            ft.DataColumn(
                ft.Text("ID")
            ),


            ft.DataColumn(
                ft.Text("Nombre")
            ),


            ft.DataColumn(
                ft.Text("Apellido P.")
            ),


            ft.DataColumn(
                ft.Text("Apellido M.")
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


    # ==========================
    # LIMPIAR
    # ==========================

    def limpiar():

        nombre.value = ""

        app.value = ""

        apm.value = ""

        telefono.value = ""

        especialidad.value = ""

        disponibilidad.value = None



    # ==========================
    # CARGAR TABLA
    # ==========================

    def cargar():

        tabla.rows.clear()


        lista_djs = dao.obtener_todo()



        for dj in lista_djs:


            tabla.rows.append(

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

                                dj.app

                            )

                        ),



                        ft.DataCell(

                            ft.Text(

                                dj.apm

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

                            ft.Container(

                                width=130,


                                content=ft.Row(

                                    [


                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            icon_color=ft.Colors.BLUE_400,

                                            tooltip="Editar DJ",

                                            on_click=lambda e, d=dj: editar(d)

                                        ),



                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar DJ",

                                            on_click=lambda e, d=dj: eliminar(d)

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



    # ==========================
    # MOSTRAR FORMULARIO
    # ==========================

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

                        especialidad,

                        disponibilidad

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




    # ==========================
    # CERRAR FORMULARIO
    # ==========================

    def cerrar_formulario(e=None):


        formulario.visible = False


        limpiar()


        page.update()




    # ==========================
    # NUEVO DJ
    # ==========================

    def nuevo_dj(e):


        nonlocal dj_actual


        dj_actual = None


        limpiar()


        mostrar_formulario(

            "Nuevo DJ"

        )




    # ==========================
    # GUARDAR DJ
    # ==========================

    def guardar(e):


        try:


            nuevo = Dj(

                id_dj=dao.obtener_ultimo_id()+1,


                nombre=nombre.value,


                app=app.value,


                apm=apm.value,


                telefono=telefono.value,


                especialidad=especialidad.value,


                disponibilidad=True

                if disponibilidad.value == "Disponible"

                else False

            )



            dao.insertar(nuevo)



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "DJ agregado correctamente"

            )



        except Exception as error:


            mostrar_mensaje(

                f"Error: {error}"

            ) 

    # ==========================
    # EDITAR DJ
    # ==========================

    def editar(dj):

        nonlocal dj_actual


        dj_actual = dj



        nombre.value = dj.nombre

        app.value = dj.app

        apm.value = dj.apm

        telefono.value = dj.telefono

        especialidad.value = dj.especialidad


        disponibilidad.value = (

            "Disponible"

            if dj.disponibilidad

            else "No disponible"

        )



        mostrar_formulario(

            "Editar DJ"

        )



        formulario.content.controls[-1].controls[0].text = "Actualizar"


        formulario.content.controls[-1].controls[0].on_click = actualizar



        page.update()




    # ==========================
    # ACTUALIZAR DJ
    # ==========================

    def actualizar(e):

        try:


            dj_actual.nombre = nombre.value


            dj_actual.app = app.value


            dj_actual.apm = apm.value


            dj_actual.telefono = telefono.value


            dj_actual.especialidad = especialidad.value


            dj_actual.disponibilidad = (

                True

                if disponibilidad.value == "Disponible"

                else False

            )



            dao.actualizar(

                dj_actual

            )



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "DJ actualizado correctamente"

            )



        except Exception as error:


            mostrar_mensaje(

                f"Error al actualizar: {error}"

            )





    # ==========================
    # MENSAJES
    # ==========================

    def mostrar_mensaje(texto):


        page.snack_bar = ft.SnackBar(

            ft.Text(texto)

        )


        page.snack_bar.open = True


        page.update()





    # ==========================
    # ELIMINAR DJ
    # ==========================

    def eliminar(dj):


        def aceptar(e):


            dao.eliminar(

                dj.id_dj

            )



            dialogo_eliminar.open = False


            page.update()



            cargar()



            mostrar_mensaje(

                "DJ eliminado correctamente"

            )




        def cancelar(e):


            dialogo_eliminar.open = False


            page.update()




        dialogo_eliminar = ft.AlertDialog(

            modal=True,


            title=ft.Text(

                "Eliminar DJ"

            ),



            content=ft.Text(

                "¿Seguro que deseas eliminar este DJ?"

            ),



            actions=[



                ft.TextButton(

                    "Cancelar",

                    on_click=cancelar

                ),



                ft.ElevatedButton(

                    "Aceptar",

                    icon=ft.Icons.DELETE,

                    on_click=aceptar

                )


            ]

        )



        page.dialog = dialogo_eliminar


        dialogo_eliminar.open = True


        page.update()





    # ==========================
    # BOTÓN NUEVO DJ
    # ==========================

    boton_nuevo = ft.ElevatedButton(

        "Nuevo DJ",

        icon=ft.Icons.ADD,

        on_click=nuevo_dj

    )





    # ==========================
    # CARGAR DATOS INICIALES
    # ==========================

    cargar()





    # ==========================
    # INTERFAZ FINAL
    # ==========================

    return ft.Container(

        expand=True,

        padding=20,


        content=ft.Column(

            [


                ft.Row(

                    [


                        ft.Text(

                            "Gestión de DJs",

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