import flet as ft

from dao.empleados_dao import EmpleadosDAO
from modelos.empleados import Empleados


def empleados(page: ft.Page):

    dao = EmpleadosDAO()

    empleado_actual = None


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


    puesto = ft.TextField(
        label="Puesto",
        width=250
    )


    telefono = ft.TextField(
        label="Teléfono",
        width=250
    )



    formulario = ft.Container(

        visible=False,

        bgcolor=ft.Colors.GREY_900,

        padding=20,

        border_radius=15

    )



    # ==========================
    # TABLA EMPLEADOS
    # ==========================

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
                ft.Text("Apellido P.")
            ),


            ft.DataColumn(
                ft.Text("Apellido M.")
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



    # ==========================
    # LIMPIAR
    # ==========================

    def limpiar():

        nombre.value = ""

        app.value = ""

        apm.value = ""

        puesto.value = ""

        telefono.value = ""



    # ==========================
    # CARGAR TABLA
    # ==========================

    def cargar():

        tabla.rows.clear()


        empleados_lista = dao.obtener_todo()



        for empleado in empleados_lista:


            tabla.rows.append(

                ft.DataRow(

                    cells=[


                        ft.DataCell(

                            ft.Text(

                                str(empleado.id_empleado)

                            )

                        ),



                        ft.DataCell(

                            ft.Text(

                                empleado.nombre

                            )

                        ),



                        ft.DataCell(

                            ft.Text(

                                empleado.app

                            )

                        ),



                        ft.DataCell(

                            ft.Text(

                                empleado.apm

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

                            ft.Container(

                                width=130,


                                content=ft.Row(

                                    [


                                        ft.IconButton(

                                            icon=ft.Icons.EDIT,

                                            icon_color=ft.Colors.BLUE_400,

                                            tooltip="Editar empleado",

                                            on_click=lambda e, emp=empleado: editar(emp)

                                        ),



                                        ft.IconButton(

                                            icon=ft.Icons.DELETE,

                                            icon_color=ft.Colors.RED_400,

                                            tooltip="Eliminar empleado",

                                            on_click=lambda e, emp=empleado: eliminar(emp)

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

                        puesto

                    ]

                ),



                ft.Row(

                    [

                        telefono

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
    # NUEVO EMPLEADO
    # ==========================

    def nuevo_empleado(e):

        nonlocal empleado_actual


        empleado_actual = None


        limpiar()


        mostrar_formulario(

            "Nuevo Empleado"

        )




    # ==========================
    # GUARDAR EMPLEADO
    # ==========================

    def guardar(e):

        try:


            nuevo = Empleados(

                id_empleado=dao.obtener_ultimo_id()+1,


                nombre=nombre.value,


                app=app.value,


                apm=apm.value,


                puesto=puesto.value,


                telefono=telefono.value

            )



            dao.insertar(nuevo)



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Empleado agregado correctamente"

            )



        except Exception as error:


            mostrar_mensaje(

                f"Error: {error}"

            )





    # ==========================
    # EDITAR EMPLEADO
    # ==========================

    def editar(empleado):

        nonlocal empleado_actual


        empleado_actual = empleado



        nombre.value = empleado.nombre

        app.value = empleado.app

        apm.value = empleado.apm

        puesto.value = empleado.puesto

        telefono.value = empleado.telefono



        mostrar_formulario(

            "Editar Empleado"

        )



        formulario.content.controls[-1].controls[0].text = "Actualizar"


        formulario.content.controls[-1].controls[0].on_click = actualizar



        page.update()




    # ==========================
    # ACTUALIZAR EMPLEADO
    # ==========================

    def actualizar(e):

        try:


            empleado_actual.nombre = nombre.value


            empleado_actual.app = app.value


            empleado_actual.apm = apm.value


            empleado_actual.puesto = puesto.value


            empleado_actual.telefono = telefono.value



            dao.actualizar(

                empleado_actual

            )



            cerrar_formulario()


            cargar()



            mostrar_mensaje(

                "Empleado actualizado correctamente"

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
    # ELIMINAR EMPLEADO
    # ==========================

    def eliminar(empleado):


        def aceptar(e):

            dao.eliminar(

                empleado.id_empleado

            )


            dialogo_eliminar.open = False

            page.update()


            cargar()


            mostrar_mensaje(

                "Empleado eliminado correctamente"

            )



        def cancelar(e):

            dialogo_eliminar.open = False

            page.update()



        dialogo_eliminar = ft.AlertDialog(

            modal=True,


            title=ft.Text(

                "Eliminar empleado"

            ),


            content=ft.Text(

                "¿Seguro que deseas eliminar este empleado?"

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
    # BOTÓN NUEVO EMPLEADO
    # ==========================

    boton_nuevo = ft.ElevatedButton(

        "Nuevo Empleado",

        icon=ft.Icons.ADD,

        on_click=nuevo_empleado

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

                            "Gestión de Empleados",

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