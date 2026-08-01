import flet as ft

from dao.agencia_dao import AgenciaDAO
from modelos.agencia import Agencia



def agencia(page: ft.Page):


    dao = AgenciaDAO()


    agencia_actual = None



    # ==========================
    # CAMPOS
    # ==========================


    agencia_nombre = ft.TextField(

        label="Nombre de agencia",

        width=250

    )


    nombre = ft.TextField(

        label="Nombre responsable",

        width=250

    )


    app = ft.TextField(

        label="Apellido paterno",

        width=250

    )


    apm = ft.TextField(

        label="Apellido materno",

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


    empleados = ft.TextField(

        label="Cantidad empleados",

        width=250

    )



    formulario = ft.Container(

        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15

    )



    # ==========================
    # TABLA
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
                ft.Text("Empleados")
            ),


            ft.DataColumn(
                ft.Text("Acciones")
            )


        ],


        rows=[]

    ) 


    # ==========================
    # LIMPIAR CAMPOS
    # ==========================

    def limpiar():

        agencia_nombre.value = ""

        nombre.value = ""

        app.value = ""

        apm.value = ""

        telefono.value = ""

        correo.value = ""

        empleados.value = ""




    # ==========================
    # CARGAR TABLA
    # ==========================

    def cargar():


        tabla.rows.clear()


        lista = dao.obtener_todo()



        for item in lista:


            tabla.rows.append(

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

                            ft.Text(

                                str(item.empleados)

                            )

                        ),



                        ft.DataCell(

                            ft.Row(

                                [

                                    ft.IconButton(

                                        icon=ft.Icons.EDIT,

                                        icon_color=ft.Colors.BLUE_400,

                                        tooltip="Editar agencia",

                                        on_click=lambda e, a=item: editar(a)

                                    ),



                                    ft.IconButton(

                                        icon=ft.Icons.DELETE,

                                        icon_color=ft.Colors.RED_400,

                                        tooltip="Eliminar agencia",

                                        on_click=lambda e, a=item: eliminar(a)

                                    )


                                ],

                                spacing=8

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

                        agencia_nombre,

                        nombre

                    ]

                ),



                ft.Row(

                    [

                        app,

                        apm

                    ]

                ),



                ft.Row(

                    [

                        telefono,

                        correo

                    ]

                ),



                ft.Row(

                    [

                        empleados

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
    # NUEVA AGENCIA
    # ==========================

    def nueva_agencia(e):


        nonlocal agencia_actual


        agencia_actual = None


        limpiar()


        mostrar_formulario(

            "Nueva Agencia"

        )


    # ==========================
    # GUARDAR AGENCIA
    # ==========================

    def guardar(e):

        try:

            nueva = Agencia(

                id_agencia=dao.obtener_ultimo_id() + 1,

                agencia_nombre=agencia_nombre.value,

                nombre=nombre.value,

                app=app.value,

                apm=apm.value,

                telefono=telefono.value,

                correo=correo.value,

                empleados=int(empleados.value)

            )


            dao.insertar(nueva)


            cerrar_formulario()


            cargar()


            mostrar_mensaje(

                "Agencia registrada correctamente"

            )


        except Exception as error:


            print(

                "ERROR AL GUARDAR AGENCIA:",

                error

            )


            mostrar_mensaje(

                f"Error: {error}"

            )


    # ==========================
    # EDITAR AGENCIA
    # ==========================

    def editar(item):

        nonlocal agencia_actual

        agencia_actual = item


        agencia_nombre.value = item.agencia_nombre
        nombre.value = item.nombre
        app.value = item.app
        apm.value = item.apm
        telefono.value = item.telefono
        correo.value = item.correo
        empleados.value = str(item.empleados)


        mostrar_formulario(
            "Editar Agencia"
        )


        boton = formulario.content.controls[-1].controls[0]


        boton.text = "Guardar"

        boton.icon = ft.Icons.SAVE

        boton.on_click = actualizar

        page.update()



    # ==========================
    # ACTUALIZAR AGENCIA
    # ==========================

    def actualizar(e):

        nonlocal agencia_actual


        try:

            agencia_actual.agencia_nombre = agencia_nombre.value
            agencia_actual.nombre = nombre.value
            agencia_actual.app = app.value
            agencia_actual.apm = apm.value
            agencia_actual.telefono = telefono.value
            agencia_actual.correo = correo.value
            agencia_actual.empleados = int(empleados.value)


            dao.actualizar(
                agencia_actual
            )


            cerrar_formulario()

            cargar()


            mostrar_mensaje(
                "Agencia actualizada correctamente"
            )


        except Exception as error:

            print(
                "ERROR AL ACTUALIZAR AGENCIA:",
                error
            )


            mostrar_mensaje(
                f"Error al actualizar: {error}"
            )


    # ==========================
    # ELIMINAR AGENCIA
    # ==========================

    def eliminar(item):

        print(
            "BOTON ELIMINAR AGENCIA:",
            item.id_agencia
        )


        def aceptar(e):

            try:

                print(
                    "ELIMINANDO AGENCIA:",
                    item.id_agencia
                )


                dao.eliminar(
                    item.id_agencia
                )


                dialogo.open = False

                page.update()


                cargar()


                mostrar_mensaje(
                    "Agencia eliminada correctamente"
                )


            except Exception as error:

                print(
                    "ERROR AL ELIMINAR AGENCIA:",
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
                "Eliminar Agencia"
            ),


            content=ft.Text(
                f"¿Seguro que deseas eliminar {item.agencia_nombre}?"
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


        page.overlay.append(dialogo)

        dialogo.open = True

        page.update()



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
    # BOTON NUEVA AGENCIA
    # ==========================

    boton_nuevo = ft.ElevatedButton(

        "Nueva Agencia",

        icon=ft.Icons.ADD,

        on_click=nueva_agencia

    )




    # ==========================
    # CARGA INICIAL
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

                            "Gestión de Agencia",

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